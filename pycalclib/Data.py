
class Data():
    def __init__(self, type, value):
        self.type = type
        self.value = value

    def __eq__(self, other):
        return (self.type == other.type and
                self.value == other.value)

    def __repr__(self):
        typeName = "None"
        if self.type:
            typeName = self.type.name

        return "Data(%s, %s)" % (typeName, self.value)


class Variable():
    def __init__(self, name, data):
        self.name = name
        self.data = data

    def __eq__(self, other):
        return self.data == other.data

    def __repr__(self):
        return "Variable(%s, %s)" % (self.name, self.data)
