#!/usr/bin/env python3
# coding: utf-8

import BaseType
# import registerType de je ne sais où ?
import re


class Integer(BaseType):
    name = 'Int'

    def format(self, value):
        return int(value)

    def detect(self, value):
        '''Is value an Integer ?
            Test if value is only compose of digits from 0 to 9.
        '''
        return re.test(r'([0-9]+)', value)

    def fromBytes(self, _bytes):
        return int.from_bytes(_bytes, 'big')

    def toBytes(self, value):
        return value.to_bytes((value.bit_length() + 7) // 8, 'big')

    def toString(self, value):
        return value


# Register the type
registerType(Integer())