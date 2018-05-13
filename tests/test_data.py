from pycalclib.Data import Data, Variable
from pycalclib.Manager import Manager


def test_Data_equality():
    data1 = Data(Manager.getTypeByClassName('Integer'), 2)

    data2 = Data(Manager.getTypeByClassName('Integer'), 2)

    data3 = Data(Manager.getTypeByClassName('Integer'), 3)

    data4 = Data(Manager.getTypeByClassName('Hexadecimal'), b'\x03')

    assert data1 == data2
    assert data1 != data3
    assert data1 != data4


def test_Variable_equality():
    var1 = Variable('myVar', Data(Manager.getTypeByClassName('Integer'), 2))

    var2 = Variable('myVar', Data(Manager.getTypeByClassName('Integer'), 2))

    var3 = Variable('otherVar', Data(Manager.getTypeByClassName('Integer'), 2))

    assert var1 == var2
    assert var1 != var3
