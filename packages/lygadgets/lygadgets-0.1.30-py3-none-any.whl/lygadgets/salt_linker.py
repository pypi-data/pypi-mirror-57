from __future__ import print_function
try:  # python 2 does not have FileNotFoundError. Check it
    FileNotFoundError
except NameError:
    FileNotFoundError = IOError

import os
import subprocess
from importlib import import_module
from shutil import rmtree, copytree
from types import ModuleType

from lygadgets.markup import xml_to_dict
from lygadgets.environment import klayout_home, is_windows


def symlink_windows(source, destination):
    # API based. The easy way
    try:
        os.symlink(source, destination)
        return
    except AttributeError:
        pass

    # Command line shell
    try:
        retval = subprocess.call(['ln', '-s', source, destination])
        assert retval == 0
        return
    except (subprocess.CalledProcessError, WindowsError, AssertionError):
        pass

    # Big magic with windows-specific package
    # From https://stackoverflow.com/questions/1447575/symlinks-on-windows
    try:
        import ctypes
        csl = ctypes.windll.kernel32.CreateSymbolicLinkW
        csl.argtypes = (ctypes.c_wchar_p, ctypes.c_wchar_p, ctypes.c_uint32)
        csl.restype = ctypes.c_ubyte
        flags = 0
        if source is not None and os.path.isdir(source):
            flags = 1
        if csl(destination, source, flags) == 0:
            raise ctypes.WinError('You do not have the permission to create a symbolic link.\nTry running as administrator')
        return
    except WindowsError:
        pass

    # Otherwise it didn't work
    raise WindowsError('Failed to find a way to link to a file in windows')


def lypackage_name(source):
    try:
        with open(os.path.join(source, 'grain.xml')) as grain:
            return xml_to_dict(grain.read())['salt-grain']['name']
    except FileNotFoundError as err:
        err.args = ((source +
                     ' does not appear to be a klayout package.' +
                     'It must have a grain.xml file.\n' +
                     str(err.args[0])), ) + err.args[1:]
        raise
    except KeyError as err:
        raise FileNotFoundError((source +
                                 ' : grain.xml does not define a "name" property.'))


def is_lypackage(source):
    if not os.path.isdir(source):
        return False
    try:
        lypackage_name(source)
        return True
    except (FileNotFoundError, KeyError):
        return False


def is_pypackage(source):
    if not os.path.isdir(source):
        return False
    return os.path.exists(os.path.join(source, '__init__.py'))


def is_pymodule(source):
    if not os.path.isfile(source):
        return False
    return os.path.splitext(source)[1] == '.py'


def is_lytech(source):
    ''' In this case the "source" is the full tech directory or the .lyt file
        It always returns the tech directory path
    '''
    if os.path.isfile(source):
        if source.endswith('.lyt'):
            source = os.path.dirname(source)
        else:
            return False
    else:
        for file_obj in os.listdir(source):
            if file_obj.endswith('.lyt'):
                return source
        else:
            return False


def is_lymacro(source):
    if not os.path.isfile(source):
        return False
    if not source.endswith('.lym'):
        return False
    return True


def is_pymacro(source):
    if not is_lymacro(source):
        return False
    with open(source) as macro:
        interpreter = xml_to_dict(macro.read())['klayout-macro']['interpreter']
    return interpreter.lower() == 'python'


def is_rubymacro(source):
    return is_lymacro(source) and not is_pymacro(source)


def module_from_str(module):
    if type(module) is ModuleType:
        return module
    elif type(module) is str:
        return import_module(module)
    else:
        raise TypeError('Argument must either be a module or a string')


def is_installed_python(module):
    try:
        module_from_str(module)
        return True
    except:
        return False


def srcdir_from_any(source):
    try:
        if os.path.exists(source):
            return os.path.realpath(source)
    except TypeError:
        pass
    if is_installed_python(source):
        module = module_from_str(source)
        # now figure out if it is a package or a non-packaged module
        try:
            return module.__path__[0]
        except AttributeError:
            return module.__file__
    else:
        raise FileNotFoundError('{} does not exist'.format(source))


def dest_from_srcdir(source, exclude_python_types=False):
    if is_lypackage(source):
        link_name = lypackage_name(source)
        link_dir = os.path.join(klayout_home(), 'salt')
    elif is_lytech(source) != False:
        enclosing_dir = is_lytech(source)
        link_dir = os.path.join(klayout_home(), 'tech')
        link_name = os.path.splitext(os.path.basename(enclosing_dir))[0]
    elif is_lymacro(source):
        link_dir = os.path.join(klayout_home(), 'pymacros' if is_pymacro(source) else 'macros')
        link_name = os.path.basename(source)
    elif is_pypackage(source) or is_pymodule(source):
        if not exclude_python_types:
            link_dir = os.path.join(klayout_home(), 'python')
            link_name = os.path.basename(source)
        else:
            return None
            # raise TypeError('Python thing found but it is being excluded')
    else:
        raise TypeError('Did not recognize the klayout relevance/format of {}'.format(source))

    if not os.path.exists(link_dir):
        os.mkdir(link_dir)
    link = os.path.join(link_dir, link_name)
    return link


def link_any(any_source, overwrite=False, hard_copy=False, exclude_python_types=False):
    ''' Directories take precedence over installed python module

        Platform independent.

        Always overwrites existing symbolic links.

        Returns the full paths of source and destination if the link was created, otherwise None for both.

        If you have given it a python package or an installed module with .lym's in it, klayout will automatically find them.
        Note to make sure they come along with the pip distro, use "package_data" in setup.py
    '''
    src = srcdir_from_any(any_source)
    try:
        dest = dest_from_srcdir(src, exclude_python_types=exclude_python_types)
    except TypeError as err:
        return None, None
    if dest is None:
        return None, None

    if src == dest:
        # Prevent circular reference
        return None, None
    if os.path.islink(dest):
        os.remove(dest)
    if os.path.exists(dest):
        if overwrite:
            rmtree(dest)
        else:
            return None, None

    if hard_copy:
        copytree(src, dest)
    else:
        if not is_windows():
            os.symlink(src, dest)
        else:
            symlink_windows(src, dest)

    # __lygadget_link__ is the special top package attribute that triggers more linking.
    # A list of strings/modules that must be installed or discoverable by import_module
    if is_installed_python(any_source) or is_pypackage(any_source) or is_pymodule(any_source):
        module = module_from_str(any_source)
        try:
            others_to_link = module.__lygadget_link__
        except AttributeError:
            others_to_link = []
        for other in others_to_link:
            subsrc, subdest = link_any(other)
            if subsrc is not None:
                print('Dependency linked:', any_source, '->', other)

    return src, dest
