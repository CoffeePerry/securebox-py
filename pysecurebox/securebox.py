# coding=utf-8

class BoxAlgo:
    def __init__(self):
        pass


class BoxAlgoAES(BoxAlgo):
    def __init__(self):
        super(BoxAlgoAES, self).__init__()


class SecureBox:
    def __init__(self, file: str, algo: BoxAlgo = None):
        if file is None or (not isinstance(file, str)):
            raise Exception('file must be a filename')
        self._file = file
        self._algo = algo

    def create_box(self):
        with open(self.file, 'x'):
            pass

    def append(self, content):
        if content is None:
            return
