class Employee:
    def __init__(self):
        self.__name = ""

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

e = Employee()
e.set_name("Suraj")
print(e.get_name())