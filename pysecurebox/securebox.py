# coding=utf-8

from Cryptodome.Cipher import AES
from Cryptodome.Protocol.KDF import scrypt
from Cryptodome.Random import get_random_bytes

from base64 import b64encode, b64decode
from io import UnsupportedOperation

from typing import Tuple

FILE_SEPARATOR = '.'


class SecureBox(object):
    def __init__(self, file: str, password: str, salt: str = None):
        if file is None or (not isinstance(file, str)):
            raise Exception('file must be a filename')
        self._file = file
        self._password = password
        self._salt = salt

    def get_salt(self) -> str:
        return self._salt

    def __unzip_filedata(self, filedata: str) -> Tuple[str, str, str]:
        try:
            nonce, tag, body = filedata.split(FILE_SEPARATOR)
        except UnsupportedOperation:
            raise Exception(f'Impossible to read: {self._file}')
        if not nonce:
            raise Exception('nonce not found')
        if not tag:
            raise Exception('tag not found')
        if not body:
            raise Exception('body not found')
        return nonce, tag, body

    def derive_key(self, password: str, fast: bool = False):
        if password is None or (not isinstance(password, str) or (not password)):
            raise Exception('password param must be non empty string')
        if self._salt is None:
            self._salt = get_random_bytes(16)
        return scrypt(password, str(self._salt), 32, N=2 ** 14 if fast else 2 ** 20, r=8, p=1)

    def append(self, content):
        """Append passed content to the SecureBox file.

        :param content: Title lines.
        """
        if content is None:
            return
        with open(self._file, 'w+') as file:
            plaintext = None

            filedata = file.read()
            if filedata:
                nonce, tag, body = self.__unzip_filedata(filedata)

                plaintext = AES.new(self.derive_key(self._password), AES.MODE_OCB, nonce=b64decode(nonce)) \
                    .decrypt_and_verify(b64decode(body), b64decode(tag))

            cipher = AES.new(self.derive_key(self._password), AES.MODE_OCB)
            ciphertext, tag = cipher.encrypt_and_digest(plaintext + content if plaintext else content)
            file.write(f'{b64encode(cipher.nonce)}{FILE_SEPARATOR}{b64encode(tag)}{FILE_SEPARATOR}'
                       f'{b64encode(ciphertext)}')

    def read(self):
        """Read all SecureBox file's contents.

        :return: SecureBox file's contents.
        """
        with open(self._file, 'r') as file:
            nonce, tag, body = self.__unzip_filedata(file.read())

            return AES.new(self.derive_key(self._password), AES.MODE_OCB, nonce=b64decode(nonce)) \
                .decrypt_and_verify(b64decode(body), b64decode(tag))
