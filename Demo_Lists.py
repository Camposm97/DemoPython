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
myList.insert(0, 'Bear');
print(myList)   # I try to replace my element at 0 but Python added onto like a LinkedList
myList.remove('Campos')
print(myList)

# myList.sort() I'll get an error if i try to sort because my list contains numbers and strings
value = 22
myList.remove(value)    # Remove 22 so I can sort
# I can remove an element using a variable like in Java

# Add more elements
myList.append('Computer')
myList.append("Science")
myList.append('Apple')
print("Unsorted", myList)
myList.sort()
print("Sorted", myList)

# Another way to delete an element from my list is to use
# the del keyword and then the index of the the list
del myList[0]
print("After deletion:", myList)

# I can also call a function called pop() it returns the first element I inserted, treating
# the data structure as a stack.  Something interesting about the stack function is that
# I can pass a value in the parameters and pop a specific value at index n from the my list
value = myList.pop()
print("Popped Element:", value)
print(myList)

myList.reverse()    # There's also a function where I can reverse the list
print(myList)

# If I want to find out about the size of my list I can the len() function and
# pass my list in there to find the size
print("The current size of my list is", len(myList))

# If I wanted to sort the list without changing the list itself, I can call
# the sorted() function that returns the my list sorted
print("Temp Sort: ", sorted(myList))

