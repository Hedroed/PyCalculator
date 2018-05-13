from pycalclib.Storage import Storage
from pycalclib.Data import Data
from pycalclib.Manager import Manager


def test_storage_varaible_creation():
    st = Storage()

    var1 = st.createVariable('myVar', Data(
        Manager.getTypeByClassName('Integer'), 2))

    expectedVar = Data(Manager.getTypeByClassName('Integer'), 2)

    assert var1 == st.getVariable('myVar')
    assert var1 in st.getAllVariables()
    assert var1 == expectedVar
