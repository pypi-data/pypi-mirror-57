import os
import zipfile
import logging
from .. import helper
from .cmd_base import CmdBase

logger = logging.getLogger(__name__)


class CmdZip(CmdBase):
    """ Zip a folder and add it to the executable
    """

    def __init__(self, path, zip_name, zip_clean=True):
        super().__init__()
        if isinstance(path, list):
            self._path = os.path.join(*path)
        else:
            self._path = path
        self._path = os.path.abspath(self._path)
        self._zip_clean = zip_clean
        self._zip = zip_name

    def pre_build(self):
        zipf = zipfile.ZipFile(self._zip, 'w', zipfile.ZIP_DEFLATED)
        for root, dirs, files in os.walk(self._path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path,
                           arcname=os.path.relpath(file_path, self._path))
                logger.info("Adding file to zip: " +
                            os.path.relpath(file_path, self._path))
        zipf.close()

    def post_build(self):
        if self._zip_clean:
            os.remove(self._zip)

    def get_build_params(self):
        params = []
        params += ['--add-data', self._zip + os.path.pathsep + '.']
        return params
