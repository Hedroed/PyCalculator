"""Test iterpretor result
"""

from pycalclib.Interpretor import Interpretor, ExecutionResult, ExecutionLine, Scope
from pycalclib.Data import Data, Variable
from pycalclib.Manager import Manager
from pycalclib.Storage import Storage

from pycalclib.type.Integer import Integer
from pycalclib.type.Hexadecimal import Hexadecimal


def test_ExecutionResult_equality():
    expecedResult1 = ExecutionResult(
        Data(Manager.getTypeByClassName('Integer'), 2))

    expecedResult2 = ExecutionResult(
        Data(Manager.getTypeByClassName('Integer'), 2))

    expecedResult3 = ExecutionResult(
        Data(Manager.getTypeByClassName('Hexadecimal'), b'\x42'))

    assert expecedResult1 == expecedResult2
    assert expecedResult1 != expecedResult3


def test_basic_math_operation():
    i = Interpretor()

    res = i.interpret("1 + 1")

    expecedResult = ExecutionResult(
        Data(Manager.getTypeByClassName('Integer'), 2))

    assert res == expecedResult


def test_convertion_int_to_hex():
    i = Interpretor()

    res = i.interpret("42 to hex")

    expecedResult = ExecutionResult(
        Data(Manager.getTypeByClassName('Hexadecimal'), b'\x2a'))

    assert res == expecedResult


def test_store_in_variable():
    i = Interpretor()

    res = i.interpret("42 in var1")

    expecedResult = ExecutionResult(
        Data(Manager.getTypeByClassName('Integer'), 42))

    var = Variable('var1', Data(Manager.getTypeByClassName('Integer'), 42))

    assert res == expecedResult
    assert var in res.created_variables
    assert var == i.storage.getVariable('var1')


def test_ExecutorLine_quote_auto_completion():
    line = ExecutionLine("la phrase\" as bytes")

    assert line.line == "\"la phrase\" as bytes"


def test_ExecutorLine_parentesis_optimisation():
    line = ExecutionLine("1 + ((((2 * 2))))")

    assert line.line == "1 + (2 * 2)"


def test_scope_heap_creation():
    line = ExecutionLine("1 + 1")
    scope = Scope(line)

    assert scope.heap == ["1", "+", "1"]

    line2 = ExecutionLine("a as hex + (14 % 4)")
    scope2 = Scope(line)

    assert scope2.heap == ["a", "as", "hex", "+", "(14 % 4)"]

    line3 = ExecutionLine("\"une phrase\" as hex")
    scope3 = Scope(line)

    assert scope3.heap == ["\"une phrase\"", "as", "hex"]
