##todo##
#add negative number error handling

print('How many cats do you have?')
numCats = input()
try:
    if int(numCats) >= 4:
        print("That is a lot of cats.")
    elif int(numCats) < 0:
        print("What is a negative cat?")
    elif int(numCats) == 0:
        print("Have you thought about getting a cat?")
    else:
        print('That is not that many cats.')

except ValueError:
    print('You did not enter a number.')
