# This is a comment
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