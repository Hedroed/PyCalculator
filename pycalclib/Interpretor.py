"""
Main class, contain entry point to use the pycalc syntaxe
"""

from .Storage import Storage


class Interpretor():

    def __init__(self):
        storage = Storage()

    def interpret(self, line):
        """
        Compute a string with the pycalc syntaxe

        Args:
            line (str): The string to interpret

        Returns:
            ExecutionResult: The result of the line execution in an object

        """
        pass


class Scope():

    heap = None
    current_value = None

    def __init__(self, line):
        if type(line) is not ExecutionLine:
            raise Exception("Args line must be of type ExecutionLine")

        self.originalLine = line

    def _createInstructionHeap(self):
        """Cut the line string into separate intruction
        """
        pass

    def start():
        """Start execution of instructions of this scope.

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
    """

    def __init__(self, line):
        self.line = line

    def _countQuote():
        pass

    def _countParentesis():
        pass


class ExecutionResult():

    stacktrace = None
    created_vars = None
    used_vars = None
    used_types = None
    used_operations = None
    errors = None

    def __init__(self, current_value):
        pass

    def __eq__(self, other):
        pass
