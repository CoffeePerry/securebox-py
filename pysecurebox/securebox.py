# coding=utf-8

from Cryptodome.Cipher import AES
from Cryptodome.Protocol.KDF import scrypt
from Cryptodome.Random import get_random_bytes

from base64 import b64encode, b64decode
from io import UnsupportedOperation
from os import path

from typing import Tuple

FILE_SEPARATOR = '.'
ENCODING = 'utf-8'


class SecureBox(object):
    def __init__(self, file: str, password: str, fast_key_derivation: bool = False):
        if file is None or (not isinstance(file, str)):
            raise Exception('file must be a filename')
        self._file = file
        self._salt = None
        if path.exists(self._file):
            with open(self._file, 'r', encoding=ENCODING) as file:
                self._salt, _, _, _ = self.__unzip_file_data(file.read())
        self._fast_key_derivation = fast_key_derivation
        self._key = self.derive_key(password)

    def __unzip_file_data(self, file_data: str) -> Tuple[bytes, bytes, bytes, bytes]:
        try:
            salt, nonce, tag, body = file_data.split(FILE_SEPARATOR)
        except UnsupportedOperation:
            raise Exception(f'Impossible to read: {self._file}')
        if not nonce:
            raise Exception('nonce not found')
        if not tag:
            raise Exception('tag not found')
        if not body:
            raise Exception('body not found')
        if not salt:
            raise Exception('salt not found')
        return b64decode(salt), b64decode(nonce), b64decode(tag), b64decode(body)

    def derive_key(self, password: str):
        if password is None or (not isinstance(password, str) or (not password)):
            raise Exception('password param must be non empty string')
        if self._salt is None:
            self._salt = get_random_bytes(16)
        return scrypt(password, self._salt, 32, N=2 ** 14 if self._fast_key_derivation else 2 ** 20, r=8, p=1)

    def append(self, content):
        """Append passed content to the SecureBox file.

        :param content: Title lines.
        """
        if content is None:
            return
        plaintext = None
        if not path.exists(self._file):
            with open(self._file, 'x', encoding=ENCODING):
                pass
        else:
            plaintext = self.read()
        with open(self._file, 'r+', encoding=ENCODING) as file:
            cipher = AES.new(self._key, AES.MODE_OCB)
            cipher.update(self._key + cipher.nonce)
            ciphertext, tag = cipher.encrypt_and_digest(plaintext + content if plaintext else content)

            file.truncate(0)
            file.write(f'{b64encode(self._salt).decode(encoding=ENCODING)}{FILE_SEPARATOR}'
                       f'{b64encode(cipher.nonce).decode(encoding=ENCODING)}{FILE_SEPARATOR}'
                       f'{b64encode(tag).decode(encoding=ENCODING)}{FILE_SEPARATOR}'
                       f'{b64encode(ciphertext).decode(encoding=ENCODING)}')

    def read(self):
        """Read all SecureBox file's contents.

        :return: SecureBox file's contents.
        """
        with open(self._file, 'r', encoding=ENCODING) as file:
            file_data = file.read()
            _, nonce, tag, body = self.__unzip_file_data(file_data)

            cipher = AES.new(self._key, AES.MODE_OCB, nonce=nonce)
            cipher.update(self._key + cipher.nonce)
            return cipher.decrypt_and_verify(body, tag)
