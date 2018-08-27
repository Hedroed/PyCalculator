#!/usr/bin/env python3
# coding: utf-8

from .BaseType import BaseType
from ..Manager import Register
from base64 import b64encode, b64decode
import re


class Base64(BaseType):
    '''Base64 type
        Base64 is a group of similar binary-to-text encoding schemes
        that represent binary data in an ASCII string format by
        translating it into a radix-64 representation.
    '''
    name = 'base64'

    def format(self, value):
        '''Format string to Base64'''

        ret = re.match('^(?b64:)?([A-Za-z0-9+/]*={0,2})$', value)
        if ret is None:
            raise Exception("Not a base64: %s" % value)

        value = ret.group(1)
        print('OK: %s' % value)

        return value.encode()

    def detect(self, value):
        '''Is value a base64 string ?
            A base64 string is composed of uppercase and lowercase letters,
            digits (O to 9), +, / and =.
            Auto detect if start with 'b64:'
        '''
        return re.match('^b64:[A-Za-z0-9+/]*={0,2}$', value) is not None

    def fromBytes(self, _bytes):
        '''Convert bytes to base64'''
        return b64encode(_bytes)

    def toBytes(self, _bytes):
        '''Convert base64 to bytes'''
        return b64decode(_bytes)

    def toString(self, value):
        '''Return value (base64) as string'''
        return value.decode()


# Register the type
Register.registerType(Base64())
