myList = []     # Wow this a list
print('Empty List', myList)   # Empty list

# Something cool about python is that I don't have to set the size of the list like in
# Java when creating arrays.  I think Python only has lists since it's a high level
# programming language.

# If I wanted I can add onto the list using the function append()
myList.append("Noi")
print(myList)       # Display list
myList.append(1)    # I can add any kind of data type into the list
print(myList)       # Display list

# I can have access a specific element like I can in Java
myList[0] = "Michael".upper()   # Something you can do in Java too
myList[1] = 22

# myList[2] = 'Campos'    # Gives error since the list has a size of 2
# In other words, a list can have a max size

myList.append("Campos")
print(myList)
print("Ths size of my list is", myList.__len__())   # Weird function to get size of list
myList.insert(0, 'Campos');
print(myList)   # I try to replace my element at 0 but Python added onto like a LinkedList
myList.remove('Campos')
print(myList)
# myList.sort() I'll get an error if i try to sort because my list contains numbers and strings
myList.remove(22)
myList.append('Computer')
myList.append("Science")
myList.append('Apple')
print("Unsorted", myList)
myList.sort()
print("Sorted", myList)
