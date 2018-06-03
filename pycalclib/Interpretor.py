"""
Main class, contain entry point to use the pycalc syntax
"""

from .Storage import Storage
from .Data import Data, Variable
from .Manager import Register

from .operator.Addition import Addition
from .type.Base64 import Base64
from .type.Hexadecimal import Hexadecimal
from .type.Integer import Integer
from .type.String import String


class Interpretor():

    def __init__(self):
        storage = Storage()

    def interpret(self, line):
        """
        Compute a string with the pycalc syntax

        Args:
            line (str): The string to interpret

        Returns:
            ExecutionResult: The result of the line execution in an object

        """
        pass


class Scope():
    """The scope represente a level of execution.

    This is all the instruction to execute from left to right.
    If a group of instructions are in parentesis, a new inner scope is created,
    this new scope is placed in the instruction heap like an instruction.

    current_value store the value return by the last set of instruction.

    Exemples:
        1 + 1 -> at the end current_value is (2, Integer)

        145 -> at the end current_value is (145, Integer)

    Args:
        line (ExecutionLine): The line of instructions of this scope
        storage (Storage): The global storage to store and get variables

    """

    heap = None
    current_value = None

    def __init__(self, line, storage):
        if type(line) is not ExecutionLine:
            raise Exception("Args line must be of type ExecutionLine")

        self.line = line
        self.storage = storage

        self._createInstructionHeap()

    def _createInstructionHeap(self):
        """Cut the line string into separate intruction and put them in heap.

        If get instruction in parentesis created a inner scope
        with value into parentesis as instruction line.

        Heap can contain String or inner Scope.
        """
        self.heap = []

        instructions = reversed(self.line.split())
        for i in instructions:
            if i.startswith("(") and i.endswith(")"):
                innerLine = i[1:-1]
                if innerLine != "":
                    innerLineEx = ExecutionLine(innerLine)
                    self.heap.append(Scope(innerLineEx, self.storage))
            else:
                self.heap.append(i)

    def run(self):
        """Execute instructions of the heap of this scope.

        If an instruction is a scope (insttruction with parentesis),
        it will create a Scope and run it.

        Returns:
            ExecutionResult: the result of execution of the scope.
        """

        while len(self.heap) > 0:
            inst = self.heap.pop()
            print("Exec %s" % inst)

            ops = Register.getOperatorsBySymbols(inst)

            ops_cnt = len(ops)
            if ops_cnt >= 1:
                if ops_cnt > 1:
                    raise Exception("Multiple operation found %s" % ops)
                op = ops[0]
                print("Operator %s" % op)

            else:
                dataTypes = Register.getValueType(inst)

                if len(dataTypes) == 0:
                    raise Exception("No type for value %s" % inst)
                elif len(dataTypes) > 1:
                    raise Exception(
                        "Multiple type for value %s: %s" % (inst, dataTypes))

                dataType = dataTypes[0]
                value = Data(dataType, dataType.format(inst))

                print("Data %s" % value)


class ExecutionLine():
    """Contain the string to interpret

    It can auto complete line who missing the first quote by counting the number of unescaped quote
    and if it's odd add a quote a the start of the line.

    This object check that the number of parentesis and quote is even.
    Else raise an error

    TODO: Optimise parentesis: remove useless parentesis like (( something )) to ( something )
    """

    def __init__(self, line):
        self.original = line

        self._applyCorrection()

    def _countQuote(self):
        """Maybe useless.
        """
        escaped = False
        ret = 0

        for i, v in enumerate(self.line):
            if v == '\\':
                escaped = True
                continue
            if escaped:
                escaped = False
                continue

            if v == '"':
                ret += 1

        return ret

    def _countParentesis(self):
        """Maybe useless.
        """
        pass

    def _applyCorrection(self):
        self.line = self.original

        if self._countQuote() % 2 == 1:
            self.line = '"' + self.line

    def split(self):
        """Split the line at space character.

        Don't cut space in parentesis and in quote.
        """
        ret = []

        parentesisDepth = 0
        inQuote = False
        escaped = False

        lastEspace = 0

        line = str(self.line)
        for i, v in enumerate(self.line):
            if v == '\\':
                escaped = True
                continue
            if escaped:
                escaped = False
                continue

            if v == ' ' and parentesisDepth == 0 and not inQuote:
                ret.append(self.line[lastEspace:i])
                lastEspace = i + 1

            if v == '(':
                parentesisDepth += 1
            elif v == ')':
                parentesisDepth -= 1
            elif v == '"':
                inQuote = not inQuote

        ret.append(self.line[lastEspace:])
        return ret

    def getLine(self):
        """Return the line with correction.
        """
        return self.line

    def getOriginalLine(self):
        """Return the line with NO correction.
        """
        return self.original


class ExecutionResult():

    original_line = None
    line = None

    stacktrace = None
    created_vars = None
    used_vars = None
    used_types = None
    used_operations = None
    errors = None

    def __init__(self, current_value):
        pass

    def __eq__(self, other):
        """Equality of result value
        """
        pass

    def merge(self, result):
        """Concat tow ExecutionResult.

        Used by scope to add result of an inner scope.
        """
        pass
