"""
Main class, contain entry point to use the pycalc syntaxe
"""


class Interpretor():

    def __init__(self):
        storage = Storage()

    def interpret(line):
        """
        Compute a string with the pycalc syntaxe

        Args:
            line (str): The string to interpret

        Returns:
            ExecutionResult: The result of the line execution in an object

        """
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
