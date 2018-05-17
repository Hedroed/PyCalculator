#!/usr/bin/env python3
# coding: utf-8

from .BaseType import BaseType
from ..Manager import Register


class String(BaseType):
    '''String type
        A string is a sequence of characters.
        A character can be anything, as well an unprintable character.
    '''
    name = 'str'

    def format(self, value):
        '''Format string to string'''
        return value

    def detect(self, value):
        '''Is value a String ?
            We consider everything is a String
        '''
        return True

    def fromBytes(self, _bytes):
        '''Convert bytes to String'''
        return _bytes.decode()

    def toBytes(self, value):
        '''Convert String to bytes'''
        return value.encode()

    def toString(self, value):
        '''Return value as string'''
        return value


# Register the type
Register.registerType(String())
