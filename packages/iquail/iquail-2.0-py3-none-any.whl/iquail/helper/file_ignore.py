from fnmatch import fnmatch
import os
import shutil
import logging

logger = logging.getLogger(__name__)


def accept_path(path, ignore_list):
    """ Check if path should be ignored according to ignore_list
    ignore_list should be a list of ignore
    Example:
    [ "*.py", "!*/test.py"]
    will ignore all path ending with ".py" except
    all files named "test.py"
    """

    def not_pattern(ignore_pattern):
        if ignore_pattern.startswith('!'):
            return ignore_pattern[1:]
        return '!' + ignore_pattern

    # TODO option to keep old config if new config is provided by solution
    accept = True
    for ignore in ignore_list:
        if ignore != "":
            not_ignore = not_pattern(ignore)
            if fnmatch(path, ignore) ^ fnmatch(path, not_ignore):
                accept = fnmatch(path, not_ignore)
                logger.debug("Accepted: %s : %s" % (path, not_ignore))

    return accept


def _format_lines(line):
    line = line.split("#")[0]  # remove comments
    line = line.replace(" ", "")  # remove all spaces
    return line


class FileIgnore:
    def __init__(self, file_path):
        try:
            with open(file_path, 'r') as f:
                lines = f.read().splitlines()
        except FileNotFoundError:
            lines = []
        self._ignore_list = list(map(_format_lines, lines))

    def accept(self, path):
        return accept_path(path, self._ignore_list)

    def copy_ignored(self, src, dest):
        """Move all ignored files"""
        for root, _, files in os.walk(src):
            for f in files:
                rel_root = os.path.relpath(root, src)
                file_path = os.path.join(root, f)
                dest_path = os.path.join(dest, rel_root)
                if not self.accept(os.path.join(rel_root, f)):
                    logger.debug("Copying %s to %s" %
                                 (file_path, os.path.join(dest_path, f)))
                    os.makedirs(dest_path, 0o777, True)
                    shutil.copy(file_path, os.path.join(dest_path, f))
