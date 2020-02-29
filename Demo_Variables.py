import math
# Imports by conventions are at the top of the file
'Another way to make a comment'
# No need to declare the data type anymore.
# You just need to declare the name of the
# variable and set it equal to whatever you want it to be.

firstName = "Michael"
lastName = "Campos"
fullName = firstName + " " + lastName

# Another thing to note is that when declaring strings
# you have a choice to either use single or double
# quotation marks.
msg1 = 'I am'
msg2 = 'years old'

# Note: In java we don't really use underscore for naming variables or methods.
# In Python, they use camel case and under scores

age = 22

print("My name is: " + fullName)
print("UPPER: " + fullName.upper())
print("lower: " + fullName.lower())
print("Title: " + fullName.title())
print(msg1 + ' ' + str(age) + ' ' + msg2)

# Something to notice is that in java if you want to print a string
# and append it with a number you jut have to use + to add the number.
# However, in python you have to use their str() function to parse the int
# to a string.

# I want to make numbers
x = 7
y = 21
print("x + y =", x + y)
print("x - y =", x - y)
print("x * y =", x * y)
print("x / y =", x / y)
print("x // y =", x // y)   # Floor Division, something Java doesn't have
print("x % y =", x % y)

# I want to make a floating point number
pi = math.pi
print("math.pi = ", pi)
# If you don't want to append to the string you can also put a comma after the
# end of the string and pass the number there.
# For example, if I wanted to print my age with the messages I would do this:
print("Printing using commas:")
print(msg1, age, msg2)
# By default, pythons adds spaces between the variables you're printing
# Also something important to notice is that the print() function
# prints a new line after.
print("Done.")  # End of Program
