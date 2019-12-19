#   Jordan Chou
#   Dec. 19, 2019
#   A binary search algorithm

from random import randint

def inputNumber(message):
    while True:
        try:
            userInput = int(input(message))
        except ValueError:
            print("Not an integer! Try again\n")
            continue
        else:
            return userInput
            break

print("Binary Search Algorithm\n")

# Generate random numbers with difference of 2
numbers = []
numbers.append(randint(2,98))


print("Generating 100 numbers...")
while len(numbers) < 100:
    if numbers[len(numbers)-1] < 2:
        numbers.append(numbers[len(numbers)-1] + 2)
    elif numbers[len(numbers)-1] > 98:
        numbers.append(numbers[len(numbers)-1] - 2)
    else:
        sign = 0
        while sign == 0:
            sign = randint(-1, 1)
        numbers.append(numbers[len(numbers)-1] + sign*2)

print("Generated " + str(len(numbers)) + " numbers\n")
numbers.sort()

print(numbers)
while True: # Loop until user chooses to exit
    # Ask user for a number
    while True:
        userNum = inputNumber("Check if a number between 0 and 100 is in the list: ")
        if userNum < 0 or userNum > 100:
            print("Please enter a number between 0 and 100. Try again\n")
        else:
            break

    subArray = numbers[:]   # create a subArray

    # Start Binary Search Algorithm
    while len(subArray) > 1:
        halfSize = int(len(subArray)/2)
        if userNum == subArray[halfSize]:   # Check if middle is userNum
            print("\n\t" + str(userNum) + " is in the list\n")
            break
        elif userNum < subArray[halfSize]:
            subArray = subArray[:halfSize]
        else:
            subArray = subArray[halfSize:]
    # End Binary Search Algorithm

    if len(subArray) <= 1:
        print("\n\t" + str(userNum) + " cannot be found in the list\n")

    while True:
        searchAgain = input("Would you like to search for another number? ").lower()
        if (searchAgain[0] == "y"):
            break
        elif (searchAgain[0] == "n"):
            exit()
        else:
            print("Invalid entry. Try again\n")
