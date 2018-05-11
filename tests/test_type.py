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
    pass


def test_Hexadecimal_detect():
    pass


def test_Hexadecimal_fromBytes():
    pass


def test_Hexadecimal_toBytes():
    pass


def test_Hexadecimal_toString():
    pass
