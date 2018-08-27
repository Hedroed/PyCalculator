"""
The manager contain the list of all available Operators, Types and Functions.

It provide methods to register new elements.
It is used by Interpretor to get correct elements by name.
"""
from typing import List, Optional

from .type.BaseType import BaseType
from .operator.BaseOperator import BaseOperator


class Manager():
    """Manager
    """
    typesClass: List[BaseType] = []

    operatorsClass: List[BaseOperator] = []

    def registerOperator(self, operator: BaseOperator) -> bool:
        if operator in self.operatorsClass:
            return False

        if not issubclass(operator.__class__, BaseOperator):
            raise Exception(
                "Class %s is not a subclass of BaseOperator" % operator)

        if operator.length < 1:
            raise Exception(
                "Operator %s length must be more then 0" % operator)

        self.operatorsClass.append(operator)

        return True

    def registerType(self, type: BaseType) -> bool:
        if type in self.typesClass:
            return False

        if not issubclass(type.__class__, BaseType):
            raise Exception("Class %s is not a subclass of BaseType" % type)

        self.typesClass.append(type)

        return True

    def getOperatorsBySymbols(self, name: str) -> List[BaseOperator]:
        ret = []
        for op in self.operatorsClass:
            if name in op.symbols:
                ret.append(op)

        return ret

    def getTypesByName(self, name: str) -> List[BaseType]:
        ret = []
        for t in self.typesClass:
            if t.name == name:
                ret.append(t)

        return ret

    def getValueType(self, data: str) -> List[BaseType]:
        ret = []

        for _type in self.typesClass:
            if _type.detect(data):
                ret.append(_type)

        return ret

    def getTypeByClassName(self, name: str) -> Optional[BaseType]:
        for t in self.typesClass:
            if t.__class__.__name__ == name:
                return t
        return None

    def getOperatorByClassName(self, name: str) -> Optional[BaseOperator]:
        for op in self.operatorsClass:
            if op.__class__.__name__ == name:
                return op
        return None


Register = Manager()
