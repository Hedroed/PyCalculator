"""Test iterpretor result
"""

from pycalclib.Interpretor import Interpretor, ExecutionResult, ExecutionLine, Scope
from pycalclib.Data import Data, Variable
from pycalclib.Manager import Register
from pycalclib.Storage import Storage

from pycalclib.type.Integer import Integer
from pycalclib.type.Hexadecimal import Hexadecimal


def test_ExecutionResult_equality():
    expecedResult1 = ExecutionResult(
        Data(Register.getTypeByClassName('Integer'), 2))

    expecedResult2 = ExecutionResult(
        Data(Register.getTypeByClassName('Integer'), 2))

    expecedResult3 = ExecutionResult(
        Data(Register.getTypeByClassName('Hexadecimal'), b'\x42'))

    assert expecedResult1 == expecedResult2
    assert expecedResult1 != expecedResult3


def test_basic_math_operation():
    i = Interpretor()

    res = i.interpret("1 + 1")

    expecedResult = ExecutionResult(
        Data(Register.getTypeByClassName('Integer'), 2))

    assert res == expecedResult


def test_conversion_int_to_hex():
    i = Interpretor()

    res = i.interpret("42 to hex")

    expecedResult = ExecutionResult(
        Data(Register.getTypeByClassName('Hexadecimal'), b'\x2a'))

    assert res == expecedResult


def test_store_in_variable():
    i = Interpretor()

    res = i.interpret("42 in var1")

    expecedResult = ExecutionResult(
        Data(Register.getTypeByClassName('Integer'), 42))

    var = Variable('var1', Data(Register.getTypeByClassName('Integer'), 42))

    assert res == expecedResult
    assert var in res.created_variables
    assert var == i.storage.getVariable('var1')


def test_ExecutorLine_quote_auto_completion():
    line = ExecutionLine("la phrase\" as bytes")

    assert line.line == "\"la phrase\" as bytes"


def test_ExecutorLine_parentesis_optimisation():
    line = ExecutionLine("1 + ((((2 * 2))))")

    assert line.line == "1 + (2 * 2)"


def test_ExecutorLine_split():
    line = ExecutionLine(
        "\"a text example\" as bytes * (0b11111111 % a as hex)")

    split = line.split()

    assert split == ["\"a text example\"", "as",
                     "bytes", "*", "(0b11111111 % a as hex)"]

    line = ExecutionLine("\(\\\" as hex")

    split = line.split()

    assert split == ["\(\\\"", "as", "hex"]

    line = ExecutionLine(" 1     +       1   ")

    split = line.split()

    assert split == ["1", "+", "1"]


def test_scope_heap_creation():
    line = ExecutionLine("1 + 2")
    scope = Scope(line, Storage())

    assert scope.heap == ["2", "+", "1"]

    line2 = ExecutionLine("a as hex + (14 % 4)")
    scope2 = Scope(line2, Storage())

    assert type(scope2.heap[0]) is Scope
    assert scope2.heap[0].line.getOriginalLine() == "14 % 4"

    line3 = ExecutionLine("\"une phrase\" as hex")
    scope3 = Scope(line3, Storage())

    assert scope3.heap == ["hex", "as", "\"une phrase\""]


def test_scope_run():
    line = ExecutionLine("1 + 1")
    scope = Scope(line, Storage())
    res = scope.run()

    expecedResult = ExecutionResult(
        Data(Register.getTypeByClassName('Integer'), 2))

    print(res.show())

    assert res == expecedResult
