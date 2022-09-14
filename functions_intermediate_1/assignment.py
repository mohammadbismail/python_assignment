import random


def randInt(minVal=0, maxVal=100):

    if maxVal < 0 or minVal > maxVal:
        return "Wrong Parameters"
    else:
        num = random.random() * (maxVal - minVal) + minVal

    return int(num)


print(randInt())  # should print a random integer between 0 to 100
print(randInt(maxVal=50))  # should print a random integer between 0 to 50
print(randInt(minVal=50))  # should print a random integer between 50 to 100
print(randInt(minVal=50, maxVal=500))  # should print a random integer between 50 and 500
print(randInt(maxVal=-1))
print(randInt(minVal=50, maxVal=20))
