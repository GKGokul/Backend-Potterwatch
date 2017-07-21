from random import randint

array = []


# Generating a random number
def generatenumber():
    while len(array) < 10:
        randomNumber = (randint(1, 10))
        if ((randomNumber in array) or randomNumber == None):
            generatenumber()
        else:
            array.append(randomNumber)


def TheFunction():
    generatenumber()
    b = array[:]
    del array[:]
    return b
