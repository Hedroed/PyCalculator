#!/usr/bin/env python3
# coding: utf-8

from .BaseOperator import BaseOperator
from ..Manager import Register


class Addition(BaseOperator):
    default = 'Int'
    symbols = ['+']

    def __init__(self):
        # self.registerOperationFor('Hex', self.hexOp)
        pass

    def compute(self, first, second):
        return first + second

    def hexOp(self, first, second):
        return first + second


# Register the operator
Register.registerOperator(Addition())
