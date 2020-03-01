from model import Campos

# In Python, naming methods are always lower cased and underscores used for spaces


def display_student(s):
    print("My name is", s.name.get_full_name())
    print("My major is", s.major)
    print("My GPA is", s.gpa)
    print()


name = Campos.Name('Jon', 'Doe')        # Create Name object
s = Campos.Student(name, 'CSE', 3.9)    # Create Student object
display_student(s)  # Display student

# Modify attributes of student object
s.name.first = 'Jane'
s.major = 'CST'
display_student(s)  # Display student



