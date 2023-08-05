import os
import shutil

import six

from conans.client import tools
from conans.client.cmd.export import export_recipe, export_source
from conans.errors import ConanException, ConanExceptionInUserConanfileMethod, \
    conanfile_exception_formatter
from conans.model.conan_file import get_env_context_manager
from conans.model.scm import SCM, get_scm_data
from conans.paths import CONANFILE, CONAN_MANIFEST, EXPORT_SOURCES_TGZ_NAME, EXPORT_TGZ_NAME
from conans.util.files import (set_dirty, is_dirty, mkdir, rmdir, set_dirty_context_manager,
                               merge_directories)


def complete_recipe_sources(remote_manager, cache, conanfile, ref, remotes):
    """ the "exports_sources" sources are not retrieved unless necessary to build. In some
    occassions, conan needs to get them too, like if uploading to a server, to keep the recipes
    complete
    """
    sources_folder = cache.package_layout(ref, conanfile.short_paths).export_sources()
    if os.path.exists(sources_folder):
        return None

    if conanfile.exports_sources is None:
        mkdir(sources_folder)
        return None

    # If not path to sources exists, we have a problem, at least an empty folder
    # should be there
    current_remote = cache.package_layout(ref).load_metadata().recipe.remote
    if current_remote:
        current_remote = remotes[current_remote]
    if not current_remote:
        raise ConanException("Error while trying to get recipe sources for %s. "
                             "No remote defined" % str(ref))

    export_path = cache.package_layout(ref).export()
    remote_manager.get_recipe_sources(ref, export_path, sources_folder, current_remote)


def config_source_local(src_folder, conanfile, conanfile_path, hook_manager):
    """ Entry point for the "conan source" command.
    """
    conanfile_folder = os.path.dirname(conanfile_path)

    def get_sources_from_exports():
        if conanfile_folder != src_folder:
            _run_local_scm(conanfile, conanfile_folder, src_folder, output=conanfile.output)
            conanfile.output.info("Executing exports to: %s" % src_folder)
            export_recipe(conanfile, conanfile_folder, src_folder)
            export_source(conanfile, conanfile_folder, src_folder)

    _run_source(conanfile, conanfile_path, src_folder, hook_manager, reference=None, cache=None,
                get_sources_from_exports=get_sources_from_exports)


def config_source(export_folder, export_source_folder, scm_sources_folder,
                  src_folder, conanfile, output, conanfile_path, reference, hook_manager, cache):
    """ Implements the sources configuration when a package is going to be built in the
    local cache.
    """

    def remove_source(raise_error=True):
        output.warn("This can take a while for big packages")
        try:
            rmdir(src_folder)
        except BaseException as e_rm:
            set_dirty(src_folder)
            msg = str(e_rm)
            if six.PY2:
                msg = str(e_rm).decode("latin1")  # Windows prints some chars in latin1
            output.error("Unable to remove source folder %s\n%s" % (src_folder, msg))
            output.warn("**** Please delete it manually ****")
            if raise_error or isinstance(e_rm, KeyboardInterrupt):
                raise ConanException("Unable to remove source folder")

    if is_dirty(src_folder):
        output.warn("Trying to remove corrupted source folder")
        remove_source()
    elif conanfile.build_policy_always:
        output.warn("Detected build_policy 'always', trying to remove source folder")
        remove_source()

    if not os.path.exists(src_folder):  # No source folder, need to get it
        with set_dirty_context_manager(src_folder):
            mkdir(src_folder)

            def get_sources_from_exports():
                # First of all get the exported scm sources (if auto) or clone (if fixed)
                _run_cache_scm(conanfile, scm_sources_folder, src_folder, output)
                # so self exported files have precedence over python_requires ones
                merge_directories(export_folder, src_folder)
                # Now move the export-sources to the right location
                merge_directories(export_source_folder, src_folder)

            _run_source(conanfile, conanfile_path, src_folder, hook_manager, reference,
                        cache, get_sources_from_exports=get_sources_from_exports)


def _run_source(conanfile, conanfile_path, src_folder, hook_manager, reference, cache,
                get_sources_from_exports):
    """Execute the source core functionality, both for local cache and user space, in order:
        - Calling pre_source hook
        - Getting sources from SCM
        - Getting sources from exported folders in the local cache
        - Clean potential TGZ and other files in the local cache
        - Executing the recipe source() method
        - Calling post_source hook
    """
    conanfile.source_folder = src_folder
    conanfile.build_folder = None
    conanfile.package_folder = None
    with tools.chdir(src_folder):
        try:
            with get_env_context_manager(conanfile):
                hook_manager.execute("pre_source", conanfile=conanfile,
                                     conanfile_path=conanfile_path,
                                     reference=reference)
                output = conanfile.output
                output.info('Configuring sources in %s' % src_folder)
                get_sources_from_exports()

                if cache:
                    _clean_source_folder(src_folder)  # TODO: Why is it needed in cache?
                with conanfile_exception_formatter(conanfile.display_name, "source"):
                    conanfile.source()

                hook_manager.execute("post_source", conanfile=conanfile,
                                     conanfile_path=conanfile_path,
                                     reference=reference)
        except ConanExceptionInUserConanfileMethod:
            raise
        except Exception as e:
            raise ConanException(e)


def _clean_source_folder(folder):
    for f in (EXPORT_TGZ_NAME, EXPORT_SOURCES_TGZ_NAME, CONANFILE+"c",
              CONANFILE+"o", CONANFILE, CONAN_MANIFEST):
        try:
            os.remove(os.path.join(folder, f))
        except OSError:
            pass
    try:
        shutil.rmtree(os.path.join(folder, "__pycache__"))
    except OSError:
        pass


def _run_cache_scm(conanfile, scm_sources_folder, src_folder, output):
    """
    :param conanfile: recipe
    :param src_folder: sources folder in the cache, (Destination dir)
    :param scm_sources_folder: scm sources folder in the cache, where the scm sources were exported
    :param output: output
    :return:
    """
    scm_data = get_scm_data(conanfile)
    if not scm_data:
        return

    if scm_data.subfolder:
        dest_dir = os.path.normpath(os.path.join(src_folder, scm_data.subfolder))
    else:
        dest_dir = src_folder
    if os.path.exists(scm_sources_folder):
        output.info("Copying previously cached scm sources")
        merge_directories(scm_sources_folder, dest_dir)
    else:
        output.info("SCM: Getting sources from url: '%s'" % scm_data.url)
        scm = SCM(scm_data, dest_dir, output)
        scm.checkout()
        # This is a bit weird. Why after a SCM should we remove files.
        # Maybe check conan 2.0
        # TODO: Why removing in the cache? There is no danger.
        _clean_source_folder(dest_dir)


def _run_local_scm(conanfile, conanfile_folder, src_folder, output):
    """
    Only called when 'conan source' in user space
    :param conanfile: recipe
    :param src_folder: specified src_folder
    :param conanfile_folder: Folder containing the local conanfile
    :param output: Output
    :return:
    """

    scm_data = get_scm_data(conanfile)
    if not scm_data:
        return
    dest_dir = os.path.normpath(os.path.join(src_folder, scm_data.subfolder or ""))
    # In user space, if revision="auto", then copy
    if scm_data.capture_origin or scm_data.capture_revision:  # FIXME: or clause?
        scm = SCM(scm_data, conanfile_folder, output)
        scm_url = scm_data.url if scm_data.url != "auto" else \
            scm.get_qualified_remote_url(remove_credentials=True)

        src_path = scm.get_local_path_to_url(url=scm_url)
        if src_path and src_path != dest_dir:
            excluded = SCM(scm_data, src_path, output).excluded_files
            output.info("SCM: Getting sources from folder: %s" % src_path)
            merge_directories(src_path, dest_dir, excluded=excluded)
            return

    output.info("SCM: Getting sources from url: '%s'" % scm_data.url)
    scm = SCM(scm_data, dest_dir, output)
    scm.checkout()
