def computeAge(age):
    if (age % 2) == 1:
        print("You have an odd age")
    else:
        print("You have an even age")

def askForAge():
    return int(input("Please enter your age: "))    # Parse input into integer


def askForScore():
    return int(input("Please enter your score: "))  # Parse input to integer


def computeScore(score):
    if (score <= 100) and (score >= 0): # Python uses 'and' and 'or' instead of && and ||
        if score > 90:
            return 'A'
        elif score > 80:    # else if <- in Java
            return 'B'
        elif score > 70:
            return 'C'
        elif score > 60:
            return 'D'
        else:
            return 'F'
    else:
        return 'out of range'   # Else grade is not within 0-100


age = askForAge()
computeAge(age)
score = askForScore()
grade = computeScore(score)
print("Your grade is", grade)
print("Done")

