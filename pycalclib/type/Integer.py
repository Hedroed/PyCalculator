#!/usr/bin/env python3
# coding: utf-8

from .BaseType import BaseType
from ..Manager import Register
import re


class Integer(BaseType):
    '''Integer type
        An Integer is a number that can be written without a fractional component.
        An Integer is only compose of digits from 0 to 9.
    '''
    name = 'int'

    def format(self, value):
        '''Format string to Integer'''
        return int(value)

    def detect(self, value):
        '''Is value an Integer ?
            Test if value is only compose of digits from 0 to 9.
        '''
        return re.match(r'^-?[0-9]+$', value) is not None

    def fromBytes(self, _bytes):
        '''Convert bytes to Integer using big endian'''
        return int.from_bytes(_bytes, 'big')

    def toBytes(self, value):
        '''Convert Integer to bytes using big endian'''
        return value.to_bytes(max(1, (value.bit_length() + 7) // 8), 'big')

    def toString(self, value):
        '''Return value as string'''
        return str(value)


# Register the type
Register.registerType(Integer())
