# Python Course
# Lists and Loops

names = ["Joe", "Mary", "Eugene", "Katrina"]

# print each name, one at a time:

# each time through the loop, make sure there is at least one name left
while len(names) > 0:
    # the list of names is guaranteed to be at least length one
    # so we can safely get the first item:
    name = names[0]
    # remove the first item from the list. remember this modifies
    # the list of names
    del names[0]
    # print it out, then we loop!
    print(name)
