from pycalclib.Storage import Storage
from pycalclib.Data import Data
from pycalclib.Manager import Register


def test_storage_varaible_creation():
    st = Storage()

    var1 = st.createVariable('myVar', Data(
        Register.getTypeByClassName('Integer'), 2))

    expectedVar = Data(Register.getTypeByClassName('Integer'), 2)

    assert var1 == st.getVariable('myVar')
    assert var1 in st.getAllVariables()
    assert var1 == expectedVar
