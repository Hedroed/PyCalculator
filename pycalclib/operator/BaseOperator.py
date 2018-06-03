#!/usr/bin/env python3
# coding: utf-8
from typing import List


class BaseOperator:

    default = 'str'
    symbols: List[str] = []

    def __init__(self) -> None:
        pass
