import os
import pathlib
import shutil
import atexit
import tempfile
import sys
from contextlib import suppress
from hashlib import md5
from abc import ABC, abstractmethod
from ..helper import misc
from .. import helper
from ..constants import Constants


class InstallerBase(ABC):
    """Register application on the OS"""

    def __init__(self,
                 binary,
                 name,
                 icon,
                 publisher,
                 install_systemwide=False,
                 console=False,
                 binary_options='',
                 install_path=None,
                 requires_root=False,
                 launch_with_quail=True,
                 is_large_solution=False):
        self._install_systemwide = install_systemwide
        self._launch_with_quail = launch_with_quail
        self._binary_name = binary
        self._binary_options = binary_options
        self._name = name
        self._requires_root = requires_root
        self._icon = icon
        self._publisher = publisher
        self._console = console
        self._install_path = self.build_install_path(
        ) if install_path is None else install_path
        self._solution_path = os.path.join(self._install_path, 'solution')
        self._launcher_name = "iquail_launcher"
        if self.requires_root:
            self._launcher_name = "setup_" + self._launcher_name
        if is_large_solution:
            # override tmp dir if the solution is too large
            misc.set_override_tmpdir(
                os.path.join(self.build_root_path(), "tmp-" + self.uid))

    def get_solution_icon(self):
        """Get solution's icon"""
        return self.get_solution_path(self._icon)

    @property
    def binary_name(self):
        return self._binary_name

    @property
    def icon(self):
        return self._icon

    @property
    def install_systemwide(self):
        return self._install_systemwide

    @property
    def binary_options(self):
        """Options for the binary"""
        return self._binary_options

    @property
    def launch_with_quail(self):
        """Use iquail to launch the binary
        (otherwise the shortcuts will launch the binary directly)
        """
        return self._launch_with_quail

    @property
    def requires_root(self):
        return self._requires_root

    @property
    def iquail_binary(self):
        """Get iquail executable install path"""
        script_name = helper.get_script_name()
        if "." in script_name:
            extension = script_name.split(".")[-1]
            return self.get_install_path(self._launcher_name + "." + extension)
        return self.get_install_path(self._launcher_name)

    @property
    def launch_command(self):
        return self.launcher_binary + ' ' + self.binary_options

    @property
    def launcher_binary(self):
        """Binary which will be launched by the main shortcut"""
        return self.iquail_binary if self.launch_with_quail else self.binary

    @property
    def binary(self):
        """Binary name (which must be at the root directory of your solution"""
        return os.path.realpath(self.get_solution_path(self._binary_name))

    @property
    def name(self):
        """Name of the program to be installed"""
        return self._name

    @property
    def publisher(self):
        """Information about who published the program"""
        return self._publisher

    @property
    def console(self):
        """Launch solution in console mode
        :return: boolean"""
        return self._console

    @property
    def uid(self):
        """Get application unique id"""
        uid = self.name + "-" + self.publisher
        uid = uid.replace(" ", "-")
        return uid

    def build_root_path(self):
        return os.path.join(str(pathlib.Path.home()), Constants.IQUAIL_ROOT_NAME)

    def build_install_path(self):
        """Build install path
        This function can be overridden to install files to somewhere else
        """
        return os.path.join(self.build_root_path(), self.uid)

    def get_solution_path(self, *args):
        """Get solution path"""
        return os.path.join(self._solution_path, *args)

    def get_install_path(self, *args):
        """Get install path"""
        return os.path.join(self._install_path, *args)

    def register(self):
        """Register application for the OS"""
        self._register()
        os.makedirs(self.get_install_path(), exist_ok=True)
        # install script and module:
        shutil.copy2(helper.get_script(), self.iquail_binary)
        if helper.running_from_script():
            with suppress(Exception):
                shutil.rmtree(self.get_install_path("iquail"))
            shutil.copytree(helper.get_module_path(),
                            self.get_install_path("iquail"))

    def unregister(self):
        self._unregister()
        misc.self_remove_directory(self.get_install_path())

    def registered(self):
        return os.path.isfile(self.iquail_binary) and self._unregister()

    @abstractmethod
    def _register(self):
        pass

    @abstractmethod
    def _unregister(self):
        pass

    @abstractmethod
    def _registered(self):
        pass
