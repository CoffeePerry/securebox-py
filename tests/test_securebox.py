# coding=utf-8

from pysecurebox.securebox import SecureBox, BoxAlgoAES

from os import path, makedirs

INSTANCE_DIR = 'instance'


def test_secure_box_create():
    if not path.isdir(INSTANCE_DIR):
        makedirs(INSTANCE_DIR)
    secure_box = SecureBox(path.join(INSTANCE_DIR, 'test.bin'), BoxAlgoAES())
    secure_box.create()
    assert(path.exists(path.join(INSTANCE_DIR, 'test.bin')))


def test_secure_box_append():
    if path.exists(path.join(INSTANCE_DIR, 'test.bin')):
        secure_box = SecureBox(path.join(INSTANCE_DIR, 'test.bin'), BoxAlgoAES())
        secure_box.append(b'test_1')
        secure_box.append(b'test_2')
        assert(path.exists(path.join(INSTANCE_DIR, 'test.bin')))
