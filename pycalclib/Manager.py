"""
The manager contain the list of all available Operators, Types and Functions.

It provide methods to register new elements.
It is used by Interpretor to get correct elements by name.
"""
from .type.BaseType import BaseType
from .operator.BaseOperator import BaseOperator


class Manager():
    """Manager
    """
    typesClass = []

    operatorsClass = []

    def registerOperator(self, operator):
        if operator in self.operatorsClass:
            return False

        if not issubclass(operator.__class__, BaseOperator):
            raise Exception(
                "Class %s is not a subclass of BaseOperator" % operator)

        self.operatorsClass.append(operator)

        return True

    def registerType(self, type):
        if type in self.typesClass:
            return False

        if not issubclass(type.__class__, BaseType):
            raise Exception("Class %s is not a subclass of BaseType" % type)

        self.typesClass.append(type)

        return True

    def getOperatorsByName(self, name):
        ret = []
        for op in self.operatorsClass:
            if op.name == name:
                ret.append(op)

        return ret

    def getTypesByName(self, name):
        ret = []
        for t in self.typesClass:
            if t.name == name:
                ret.append(t)

        return ret

    def getTypeByClassName(self, name):
        for t in self.typesClass:
            if t.__class__.__name__ == name:
                return t

    def getOperatorByClassName(self, name):
        for op in self.operatorsClass:
            if op.__class__.__name__ == name:
                return op


Register = Manager()
