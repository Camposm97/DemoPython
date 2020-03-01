class Person:
    def __init__(self, name):
        self.name = name
    # Person has a Name, object composition


class Student(Person):  # Student extends Person
    def __init__(self, name, major, gpa):  # Student Constructor
        super().__init__(name)  # We call super() to init the super class's constructor
        self.major = major
        self.gpa = gpa


class Name(object): # object is only need in Python 2.X
    def __init__(self, first, last):    # Name Constructor
        self.first = first
        self.last = last

    def get_full_name(self):    # Returns first and last name in one string
        return self.first + ' ' + self.last



