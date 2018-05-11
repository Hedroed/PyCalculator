"""
Storage contain local variable during program execution

It may be also store variable in file for keep data between execution

"""


class Storage():

    @staticmethod
    def fromFile(path):
        pass

    def _loadVariablesFromFile(self):
        pass

    def _saveVariablesToFile(self):
        pass

    def createVariable(self, name, value):
        pass

    def getVariable(self, name):
        pass

    def getAllVariables(self):
        pass
