# coding=utf-8

from pysecurebox.securebox import SecureBox

from os import path, makedirs, remove

DIR_INSTANCE = 'instance'
FILE_TEST = path.join(DIR_INSTANCE, 'test.box')
PASSWORD = 'secret'


def test_secure_box_overwrite_and_read():
    if not path.isdir(DIR_INSTANCE):
        makedirs(DIR_INSTANCE)
    if path.exists(FILE_TEST):
        remove(FILE_TEST)

    secure_box1 = SecureBox(FILE_TEST, PASSWORD)
    data_test1 = b'test_1'
    secure_box1.overwrite(data_test1)
    assert (path.exists(FILE_TEST))
    data_test2 = b'test_2'
    secure_box1.overwrite(data_test2)
    assert(path.exists(FILE_TEST))

    secure_box2 = SecureBox(FILE_TEST, PASSWORD)
    data = secure_box2.read()
    if path.exists(FILE_TEST):
        remove(FILE_TEST)
    assert data == data_test2


def test_secure_box_append_and_read():
    if not path.isdir(DIR_INSTANCE):
        makedirs(DIR_INSTANCE)
    if path.exists(FILE_TEST):
        remove(FILE_TEST)

    secure_box1 = SecureBox(FILE_TEST, PASSWORD)
    data_test1 = b'test_1'
    secure_box1.append(data_test1)
    assert (path.exists(FILE_TEST))
    data_test2 = b'test_2'
    secure_box1.append(data_test2)
    assert(path.exists(FILE_TEST))

    secure_box2 = SecureBox(FILE_TEST, PASSWORD)
    data = secure_box2.read()
    if path.exists(FILE_TEST):
        remove(FILE_TEST)
    assert data == (data_test1 + data_test2)


def test_secure_box_delete():
    secure_box = SecureBox(FILE_TEST, PASSWORD)
    secure_box.append(b'test')
    secure_box.delete()
    assert not path.exists(FILE_TEST)


if __name__ == '__main__':
    test_secure_box_overwrite_and_read()
    test_secure_box_append_and_read()
    test_secure_box_delete()
