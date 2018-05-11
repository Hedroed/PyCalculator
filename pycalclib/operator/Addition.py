#!/usr/bin/env python3
# coding: utf-8

import BaseOperator
# import registerOperator de je ne sais où ?


class Addition(BaseOperator):
    default = 'Int'
    symbols = ['+']

    def __init__(self):
        self.registerOperationFor('Hex', self.hexOp)


    def compute(self, first, second):
        return first + second

    def hexOp(self, first, second):
        return first + second


# Register the operator
registerOperator(Addition())