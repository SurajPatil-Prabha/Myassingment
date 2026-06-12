class Person:
    def __init__(self, name):
        self.name = name

class Patient(Person):
    def __init__(self, name, disease):
        super().__init__(name)
        self.__disease = disease

    def show(self):
        print(self.name, self.__disease)

p = Patient("Suraj", "Fever")
p.show()