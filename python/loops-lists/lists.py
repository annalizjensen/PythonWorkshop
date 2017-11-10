# Python Course
# Lists

# make a list of names:
names = ["Joe", "Mary", "Eugene", "Katrina"]

# print the whole list:
print("here is a list of names", names)
# note that print(...) can print many things, each separated by a comma
# this is a essentially a simpler way of doing:
print("here is a list of names " + str(names))

# print the length of the list:
print("the length of the list is", len(names))

# print the first item:
print("The first name in the list is", names[0])

# print the second item:
print("The second name in the list is", names[1])

# remember how we "add" strings?
x = "hello, " + "world"
print(x)

# we can do the same with lists
y = [1, 2, 3] + [9, 4, 1]
print(y)

# an easy way to "add" an item to the end of a list
cats = ["russian blue", "siamese", "burmese", "ragdoll"]
print(cats)
tabby = "tabby"
cats = cats + [tabby]
print(cats)

# del modifies a list - it does NOT create a new list
del y[1]
print(y)
