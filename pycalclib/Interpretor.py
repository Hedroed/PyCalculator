"""
Main class, contain entry point to use the pycalc syntax
"""

from .Storage import Storage


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

        self.originalLine = line
        self.storage = storage

        self._createInstructionHeap()

    def _createInstructionHeap(self):
        """Cut the line string into separate intruction and put them in heap.

        If get instruction in parentesis created a inner scope
        with value into parentesis as instruction line.

        Heap can contain String or inner Scope.
        """
        pass

    def run(self):
        """Execute instructions of the heap of this scope.

        If an instruction is a scope (insttruction with parentesis),
        it will create a Scope and run it.

        Returns:
            ExecutionResult: the result of execution of the scope.
        """
        pass


class ExecutionLine():
    """Contain the string to interpret

    It can auto complete line who missing the first quote by counting the number of unescaped quote
    and if it's odd add a quote a the start of the line.

    This object check that the number of parentesis and quote is even.
    Else raise an error

    TODO: Optimise parentesis: remove useless parentesis like (( something )) to ( something )
    """

    def __init__(self, line):
        self.line = line

    def _countQuote():
        pass

    def _countParentesis():
        pass

    def getLineString():
        """Return the line with correction.
        """
        pass


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
