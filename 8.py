class Person:
    def show(self):
        print("im person")
class Student(Person):
    def show1(self):
        print("im student")
a=Student()
a.show()
a.show1()