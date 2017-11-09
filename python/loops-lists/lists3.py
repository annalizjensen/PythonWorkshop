# Python Course
# Building a Lists and with Loops

# we will build a list of all positive number less than 21:

# start with an empty list
numbers = []

# and a counter beginning at 1
x = 1

# now we build up a list by looping
while x < 21:
    # create a tiny list that just consists of a single item -
    # the current value of x
    tiny_list = [x]
    # add it and the existsing numbers list together. remember adding list
    # creates a new list, so we put that new list back in the variable
    # called numbers
    numbers = numbers + tiny_list
    # increment x and loop
    x = x + 1

print(numbers)
