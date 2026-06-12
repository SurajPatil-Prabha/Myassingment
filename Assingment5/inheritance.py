#single inheritance 
class Parent:
    def parent_method(self):
        print("This function is in parent class.")
class Child(Parent):
    def child_method(self):
        print("This function is in child class.")
c = Child()
c.parent_method()       
c.child_method()
#multiple inheritance
class Father:       
    def father_method(self):
        print("This function is in father class.")
class Mother:
    def mother_method(self):
        print("This function is in mother class.")
class Child(Father, Mother):
    def child_method(self):
        print("This function is in child class.")
c = Child()
c.father_method()
c.mother_method()
c.child_method()
#multilevel inheritance
class Grandfather:
    def grandfather_method(self):
        print("This function is in grandfather class.")
class Father(Grandfather):
    def father_method(self):
        print("This function is in father class.")
class Child(Father):
    def child_method(self):
        print("This function is in child class.")
c = Child()
c.grandfather_method()
c.father_method()
c.child_method()
#hierarchical inheritanc
class Parent:
    def parent_method(self):
        print("This function is in parent class.")
class Son(Parent):
    def son_method(self):
        print("This function is in child1 class.")
class Daughter(Parent):
    def daughter_method(self):
        print("This function is in child2 class.")
c1 = Son()
c2 = Daughter()
c1.parent_method()
c1.son_method()
c2.parent_method()
c2.daughter_method()

