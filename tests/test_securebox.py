# coding=utf-8

from pysecurebox.securebox import SecureBox

from os import path, makedirs

INSTANCE_DIR = 'instance'
PASSWORD = 'secret'

salt = None


def test_secure_box_append():
    if not path.isdir(INSTANCE_DIR):
        makedirs(INSTANCE_DIR)
    secure_box = SecureBox(path.join(INSTANCE_DIR, 'test.bin'), PASSWORD, salt)
    secure_box.append(b'test_1')
    secure_box.append(b'test_2')
    assert(path.exists(path.join(INSTANCE_DIR, 'test.bin')))


def test_secure_box_read():
    if path.exists(path.join(INSTANCE_DIR, 'test.bin')):
        secure_box = SecureBox(path.join(INSTANCE_DIR, 'test.bin'), PASSWORD, salt)
        data = secure_box.read()
        assert data


if __name__ == '__main__':
    test_secure_box_append()
    test_secure_box_read()
