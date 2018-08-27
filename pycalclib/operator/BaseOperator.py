#!/usr/bin/env python3
# coding: utf-8
from typing import List

import abc


class BaseOperator(abc.ABC):

    default = 'str'
    symbols: List[str] = []
    length = 2

    @abc.abstractmethod
    def __init__(self):
        pass

    @abc.abstractmethod
    def compute(self, *args):
        pass

    def __repr__(self):
        return "Operator<%s>[d=%s, s='%s', l=%d]" % (self.__class__.__name__, self.default, ';'.join(self.symbols), self.length)
