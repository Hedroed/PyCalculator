from pycalclib.Manager import Manager

from pycalclib.type.Integer import Integer


def test_manager_getTypeByClassName():
    managerInt = Manager.getTypeByClassName('Integer')

    assert type(managerInt) is Integer

    managerHex = Manager.getTypeByClassName('Hexadecimal')

    assert type(managerHex) is Hexadecimal
