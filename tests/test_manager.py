from pycalclib.Manager import Register

from pycalclib.type.Integer import Integer
from pycalclib.type.Hexadecimal import Hexadecimal


def test_manager_getTypeByClassName():
    managerInt = Register.getTypeByClassName('Integer')

    assert type(managerInt) is Integer

    managerHex = Register.getTypeByClassName('Hexadecimal')

    assert type(managerHex) is Hexadecimal

    expectNone = Register.getTypeByClassName('unknowned')

    assert expectNone is None
