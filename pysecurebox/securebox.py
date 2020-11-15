# coding=utf-8

from functools import wraps


class BoxAlgo(object):
    def __init__(self):
        pass


class BoxAlgoAES(BoxAlgo):
    def __init__(self):
        super(BoxAlgoAES, self).__init__()


'''
def refresh_checksum(wrapped):
    @wraps(wrapped)
    def wrapper(self, *args, **kwargs):
        result = wrapped(self, *args, **kwargs)
        with open(self._file, 'a+b') as file:
            content = file.read()
            file.write()    # TODO...
        return result
    return wrapper
'''


class SecureBox(object):
    def __init__(self, file: str, algo: BoxAlgo = None):
        if file is None or (not isinstance(file, str)):
            raise Exception('file must be a filename')
        self._file = file
        self._algo = algo

    def create(self):
        """Create SecureBox file."""
        with open(self._file, 'x+b'):
            pass

    # @refresh_checksum
    def append(self, content):
        """Append passed content to the SecureBox file.

        :param content: Title lines.
        """
        if content is None:
            return
        with open(self._file, 'a+b') as file:
            file.write(content)

    def read_all(self):
        """Read all SecureBox file's contents.

        :return: SecureBox file's contents.
        """
        with open(self._file, 'r+b') as file:
            return file.read()
