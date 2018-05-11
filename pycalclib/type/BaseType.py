#!/usr/bin/env python3
# coding: utf-8

from abc import ABC, abstractmethod


class BaseType(abc.ABC):
    """Define a abstract Type object

    Attributes:
        name (str): The name of the type in pycalc syntaxe, if is None take the name of the class
    """

    name = None

    def getName(self):
        if self.name:
            return self.name
        else:
            return self.__class__.__name__

    @abstractmethod
    def format(self, value):
        """Transform an input value to the form which represent the value.

        The value return by format will be store in variable.

        Args:
            value (str): The input value from the interpretor.
        """
        pass

    @abstractmethod
    def detect(self, value):
        """Method used to allow pycalc to automatically detect the type of the value.

        If return True this value can be of this type.

        Args:
            value (str): The input value from the interpretor.
        """
        pass

    @abstractmethod
    def fromBytes(self, _bytes):
        """Create a value of this type from a Python primitive bytes.

        This method is call to convert types.

        Args:
            _bytes (bytes): The value in bytes to convert in this type.
        """
        pass

    @abstractmethod
    def toBytes(self, value):
        """Turn a value of this type in Python primitive bytes.

        This method is call to convert types.

        Args:
            value (any): The value to convert in bytes.
        """
        pass

    @abstractmethod
    def toString(self, value):
        """Used to convert a value of this type to this String representation.

        Call to display the value to the user.

        Args:
            value (any): A value of this type.
        """
        pass
