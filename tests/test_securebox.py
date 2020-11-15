# coding=utf-8

from pysecurebox.securebox import SecureBox

from os import path, makedirs, remove

DIR_INSTANCE = 'instance'
FILE_TEST = path.join(DIR_INSTANCE, 'test.box')
PASSWORD = 'secret'


def test_secure_box_write_read():
    if not path.isdir(DIR_INSTANCE):
        makedirs(DIR_INSTANCE)
    if path.exists(FILE_TEST):
        remove(FILE_TEST)
    secure_box = SecureBox(FILE_TEST, PASSWORD)
    secure_box.append(b'test_1')
    assert (path.exists(FILE_TEST))
    secure_box.append(b'test_2')
    assert(path.exists(FILE_TEST))
    secure_box = SecureBox(FILE_TEST, PASSWORD)
    data = secure_box.read()
    assert data == b'test_1test_2'


if __name__ == '__main__':
    test_secure_box_write_read()
