import os
from .. import helper
from .cmd_base import CmdBase


class CmdIntegrity(CmdBase):
    """ Zip a folder and add it to the executable
    """
    def __init__(self, path):
        super().__init__()
        if not isinstance(path, list):
            raise TypeError("Expected list as path")
        self._path = os.path.abspath(os.path.join(*path))

    def pre_build(self):
        verifier = helper.IntegrityVerifier(self._path)
        verifier.dump()
