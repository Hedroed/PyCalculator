#!/usr/bin/env python3
# coding: utf-8

from pycalclib.Interpretor import Scope, ExecutionLine
from pycalclib.Storage import Storage

if __name__ == '__main__':

    while True:
        line = input("Qu'est ce que tu va faire ?\n")

        print(Scope(ExecutionLine(line), Storage()).run().show())

        print("")
        print("")
