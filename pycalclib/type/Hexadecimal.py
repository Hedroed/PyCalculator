#!/usr/bin/env python3
# coding: utf-8

from .BaseType import BaseType
from ..Manager import Register
import re


class Hexadecimal(BaseType):
    '''Hexadecimal type
        Hexadecimal (also base 16, or hex) is a positional numeral system with base 16.
        Hexadecimal is composed of digits from 0 to 9 and letters from A to F.
    '''
    name = 'hex'

    def format(self, value):
        '''Format hexadecimal string to bytes'''
        _bytes = b''

        hexString = re.sub(' ', '', value)
        hexString = hexString.replace('\\x', ' ').replace('0x', ' ').split()

        for block in hexString:
            if len(block) % 2 != 0:
                block = '0' + block
            _bytes += bytearray.fromhex(block)

        return _bytes

    def detect(self, value):
        '''Is value an Hexadecimal ?
            Test if value is only compose of digits from 0 to 9 and letters from A to F.
            An hexadecimal value can preceded by '\\x' or '0x'.
            Spaces can be presents in an hexadecimal string.
        '''
        return re.match(r'^((\\x|0x)[0-9a-fA-F\s]+)+$', value) is not None

    def fromBytes(self, _bytes):
        '''Convert bytes to bytes (do nothing)'''
        return _bytes

    def toBytes(self, _bytes):
        '''Convert bytes to bytes (do nothing)'''
        return _bytes

    def toString(self, _bytes):
        '''Return value as string'''
        hexString = _bytes.hex().upper()
        return ':'.join(hexString[i:i+2] for i in range(0, len(hexString), 2))


# Register the type
Register.registerType(Hexadecimal())
