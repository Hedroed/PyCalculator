"""Main class, contain entry point to use the pycalc syntax."""

from typing import Optional, List
import datetime

from .Storage import Storage
from .Data import Data, Variable
from .Manager import Register

from .operator.Addition import Addition
from .operator.BaseOperator import BaseOperator
from .type.Base64 import Base64
from .type.Hexadecimal import Hexadecimal
from .type.Integer import Integer
from .type.String import String


class Interpretor():

    def __init__(self) -> None:
        storage = Storage()

    def interpret(self, line):
        """
        Compute a string with the pycalc syntax.

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

    heap: List[str] = []
    current_value: Optional[Data] = None

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

    def _getData(self, instruction) -> Data:
        dataTypes = Register.getValueType(instruction)
        if len(dataTypes) == 0:
            raise Exception("No type for value %s" % instruction)
        elif len(dataTypes) > 1:
            raise Exception(
                "Multiple type for value %s: %s" % (instruction, dataTypes))
        dataType = dataTypes[0]
        return Data(dataType, dataType.format(instruction))

    def _getOperation(self, instruction) -> Optional[BaseOperator]:
        ops = Register.getOperatorsBySymbols(instruction)
        ops_cnt = len(ops)
        if ops_cnt > 1:
            raise Exception("Multiple operation found %s" % ops)
        if ops_cnt == 0:
            return None
        op = ops[0]
        print("Operator %s" % op)
        return op

    def _loopExcecution(self, result: "ExecutionResult") -> None:
        while len(self.heap) > 0:
            inst = self.heap.pop()
            op = self._getOperation(inst)

            if op:
                length = op.length

                defaultTypes = Register.getTypesByName(op.default)
                # TODO: Check defaultTypes
                defaultType = defaultTypes[0]
                print("Default %s, length %d" % (defaultType, length))

                args = []
                if self.current_value:
                    args.append(self.current_value)

                for _ in range(length - len(args)):
                    inst = self.heap.pop()
                    value = self._getData(inst)
                    args.append(value)

                retType = args[0].type
                args = [value.convert(defaultType).value for value in args]

                print("Call with %s, retrun type %s" % (args, retType))
                ret = op.compute(*args)

                retData = Data(defaultType, ret)
                print('Raw ret %s' % retData)
                retData = retData.convert(retType)
                print('REt %s' % retData)
                self.current_value = retData

            else:
                value = self._getData(inst)

                print("Data %s" % value)
                self.current_value = value

        result.end_value = self.current_value

    def run(self):
        """Execute instructions of the heap of this scope.

        If an instruction is a scope (insttruction with parentesis),
        it will create a Scope and run it.

        Returns:
            ExecutionResult: the result of execution of the scope.

        """
        result = ExecutionResult()

        try:
            self._loopExcecution(result)
        except Exception as e:
            result.addException(e)

        return result


class ExecutionLine():
    """Contain the string to interpret.

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
        return [i for i in ret if i != '']  # Remove useless space

    def getLine(self):
        """Return the line with correction.
        """
        return self.line

    def getOriginalLine(self):
        """Return the line with NO correction.
        """
        return self.original


class ExecutionResult():
    """TODO."""

    def __init__(self, end_value: Optional[Data]=None) -> None:
        self.end_value = end_value

        self.creation_date = datetime.datetime.now()

        self.original_line = None
        self.line = None
        self.stacktrace = None
        self.created_vars = None
        self.used_vars = None
        self.used_types = None
        self.used_operations = None
        self.errors: List[Exception] = []

    def __eq__(self, other):
        """Equality of result value.
        """
        return self.end_value == other.end_value

    def addException(self, e: Exception):
        self.errors.append(e)

    def merge(self, result):
        """Concat tow ExecutionResult.

        Used by scope to add result of an inner scope.
        """
        pass

    def show(self):
        """Return formated information of the execution in string to display in console."""

        return """=== ExecutionResult - %s ===
- End value: %s
- Errors:%s
        """ % (
            self.creation_date.strftime("%Y-%m-%d %H:%M:%S"),
            self.end_value,
            ''.join('\n    * %s' % e for e in self.errors)
        )
