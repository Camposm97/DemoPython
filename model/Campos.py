class Student(object):  # object is only need in Python 2.X
    def __init__(self, name, major, gpa):  # Student Constructor
        self.name = name
        self.major = major
        self.gpa = gpa


class Name(object):
    def __init__(self, first, last):    # Name Constructor
        self.first = first
        self.last = last

    def get_full_name(self):    # Returns first and last name in one string
        return self.first + ' ' + self.last

