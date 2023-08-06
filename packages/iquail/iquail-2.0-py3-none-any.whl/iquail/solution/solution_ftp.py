from ftplib import FTP
import os
import shutil
from .solution_base import SolutionBase
from ..errors import SolutionUnreachableError
from ..helper import misc


class FtpWalk:
    def __init__(self, ftp, *path):
        self._ftp = ftp
        for c in path:
            self._ftp.cwd(c)
        self._path = self._ftp.pwd()

    def local(self):
        return False

    def listdir(self, _path):
        file_list, dirs, nondirs = [], [], []
        old_directory = self._ftp.pwd()
        self._ftp.cwd(_path)
        self._ftp.retrlines('LIST', lambda x: file_list.append(x.split()))
        for info in file_list:
            ls_type, name = info[0], info[-1]
            if ls_type.startswith('d'):
                if name != '..' and name != '.':
                    dirs.append(name)
            else:
                nondirs.append(name)
        self._ftp.cwd(old_directory)
        return dirs, nondirs

    def cwd(self):
        return self._path

    def walk(self, path=None):
        if not path:
            path = self._path
        dirs, nondirs = self.listdir(path)
        yield path, dirs, nondirs
        for name in dirs:
            # using cwd is the only cross platform solution I have found so far
            self._ftp.cwd(path)
            self._ftp.cwd(name)
            path = self._ftp.pwd()
            yield from self.walk(path)
            path = os.path.dirname(path)


class SolutionFtp(SolutionBase):
    def __init__(self, host, path, port=21):
        super().__init__()
        if not isinstance(path, list):
            raise TypeError("Expected list as ftp path")
        self._path = path
        self._host = host
        self._port = port
        self._tmpdir = None
        self._ftp = None
        self._files = None

    def local(self):
        return False

    def open(self):
        self._tmpdir = misc.safe_mkdtemp()
        self._ftp = FTP()
        try:
            self._ftp.connect(self._host, self._port)
            self._ftp.login()
        except Exception as e:
            self.close()
            raise SolutionUnreachableError("Can't login to ftp %s %s" %
                                           (str(self._host), str(self._port))) from e
        walk = FtpWalk(self._ftp, *self._path)
        self._files = {}
        for w in walk.walk():
            self._files[os.path.relpath(w[0], walk.cwd())] = w

    def close(self):
        self._ftp.close()
        shutil.rmtree(self._tmpdir)

    def walk(self):
        for relpath, value in self._files.items():
            yield (relpath, value[1], value[2])

    def _get_tmp_path(self, relpath):
        return os.path.join(self._tmpdir, relpath)

    def _open_tmp_file(self, relpath):
        path = self._get_tmp_path(relpath)
        os.makedirs(os.path.dirname(path), 0o777, True)
        return open(path, 'wb')

    def retrieve_file(self, relpath):
        real_path = self._files[os.path.dirname(relpath)][0]
        name = os.path.basename(relpath)
        old_directory = self._ftp.pwd()
        self._ftp.cwd(real_path)
        f = self._open_tmp_file(relpath)
        self._ftp.retrbinary("RETR %s" % name, f.write)
        f.close()
        self._ftp.cwd(old_directory)
        return self._get_tmp_path(relpath)
