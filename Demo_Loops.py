def main():     # This is a function
    name = input("What's your name? ")  # Ask user for his/her name
    nums = []
    print("Hello " + name + "!")

    for n in range(0, 5):  # Generates a list from [n1, n2)
        nums.append(n)

    # print("List:", nums)
    print("Sum of List:",sum(nums))    # There's a function called sums() to add up all the numbers in a list
    print(nums)
    # display_list(nums)

    # for n in nums:      # For every element in nums, append it to the string
    #    s1 += str(n) + " "
    #
    # print("String:", s1)

    floats = (0, 3, 1, 4, 1)
    # This is a tuple, the difference between a tuple and a list is
    # that a tuple CANNOT be modified unlike a list.
    print("Tuple:", floats)


def display_list(arr):  # Function for display list
    for n in arr:
        print(n, end=" ")
        # By using end I can now print on the same line
    print() # Print new line


main()  # Call main function
