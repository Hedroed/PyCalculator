#!/usr/bin/env python3
# coding: utf-8

from pycalclib.type.Integer import Integer
from pycalclib.type.Hexadecimal import Hexadecimal


# Integer tests

def test_Integer_format():
    i = Integer()
    assert i.format('42') == 42
    assert i.format('-26') == -26
    assert i.format('0') == 0
    assert i.format('-0') == 0


def test_Integer_detect():
    i = Integer()
    assert i.detect('42')
    assert i.detect('1190 ')
    assert i.detect(' 1190')
    assert i.detect(' 1190 ')
    assert i.detect('-34')
    assert not i.detect('5 6')
    assert not i.detect('0.45')
    assert not i.detect('4A3E')
    assert not i.detect('Hello!')


def test_Integer_fromBytes():
    i = Integer()
    assert i.fromBytes(b'\x02\x8e') == 654
    assert i.fromBytes(b'') == 0
    assert i.fromBytes(b'\x00') == 0
    assert i.fromBytes(b'\xf6') == -10


def test_Integer_toBytes():
    i = Integer()
    assert i.toBytes(654) == b'\x02\x8e'
    assert i.toBytes(0) == b''
    assert i.toBytes(-10) == b'\xf6'


def test_Integer_toString():
    i = Integer()
    assert i.toString('654') == '654'
    assert i.toString('0') == '0'
    assert i.toString('-10') == '-10'


# Hexadecimal tests

def test_Hexadecimal_format():
    h = Hexadecimal()
    assert h.format('4256') == b'\x42\x56'
    assert h.format('14256') == b'\x01\x42\x56'
    assert h.format('ABE5') == b'\xab\xe5'
    assert h.format('\\x42\\x56') == b'\x42\x56'
    assert h.format('0x4256') == b'\x42\x56'
    assert h.format('0x42\\x56') == b'\x42\x56'
    assert h.format('0x42\\x50x6') == b'\x42\x05\x06'
    assert h.format('0x60x70x80x09') == b'\x06\x07\x08\x09'
    assert h.format('\\x5\\x12\\x04') == b'\x05\x12\x04'


def test_Hexadecimal_detect():
    h = Hexadecimal()
    assert h.detect('4556')
    assert h.detect('455E6AC')
    assert h.detect('\\x42\\x56')
    assert h.detect('0x4256')
    assert h.detect('0x42\\x56')
    assert h.detect('0x60x70x80x09')
    assert h.detect('\\x5\\x12\\x04')
    assert not h.detect('4E4E4G')
    assert not h.detect('\\x4E\\x4E4G')
    assert not h.detect('0x')
    assert not h.detect('0x\\x\\x45')
    assert not h.detect('hello')
    assert not h.detect('\x00')


def test_Hexadecimal_fromBytes():
    h = Hexadecimal()
    assert h.fromBytes(b'\x42\x56') == '4256'
    assert h.fromBytes(b'\xab\xe5') == 'abe5'
    assert h.fromBytes(b'\x01\x42\x56') == '014256'
    assert h.fromBytes(b'\x42\x56') == '4256'
    assert h.fromBytes(b'\x42\x56') == '4256'
    assert h.fromBytes(b'\x42\x56') == '4256'
    assert h.fromBytes(b'\x42\x05\x06') == '420506'
    assert h.fromBytes(b'\x06\x07\x08\x09') == '06070809'
    assert h.fromBytes(b'\x05\x12\x04') == '051204'


def test_Hexadecimal_toBytes():
    h = Hexadecimal()
    assert h.toBytes('4256') == b'\x42\x56'
    assert h.toBytes('14256') == b'\x01\x42\x56'
    assert h.toBytes('ABE5') == b'\xab\xe5'
    assert h.toBytes('\\x42\\x56') == b'\x42\x56'
    assert h.toBytes('0x4256') == b'\x42\x56'
    assert h.toBytes('0x42\\x56') == b'\x42\x56'
    assert h.toBytes('0x42\\x50x6') == b'\x42\x05\x06'
    assert h.toBytes('0x60x70x80x09') == b'\x06\x07\x08\x09'
    assert h.toBytes('\\x5\\x12\\x04') == b'\x05\x12\x04'


def test_Hexadecimal_toString():
    h = Hexadecimal()
    assert h.toString(b'\x42\x56') == '42:56'
    assert h.toString(b'\xab\xe5') == 'AB:E5'
    assert h.toString(b'\x01\x42\x56') == '01:42:56'
    assert h.toString(b'\x42\x56') == '42:56'
    assert h.toString(b'\x42\x56') == '42:56'
    assert h.toString(b'\x42\x56') == '42:56'
    assert h.toString(b'\x42\x05\x06') == '42:05:06'
    assert h.toString(b'\x06\x07\x08\x09') == '06:07:08:09'
    assert h.toString(b'\x05\x12\x04') == '05:12:04'
