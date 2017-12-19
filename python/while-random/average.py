floats = []
while True:
    add = input("Add a float (or hit enter to stop): ")
    if add == "":
        break
    floats += [float(add)]

print("Here is the list of floats: %s" % str(floats))

i = 0
sumUp = 0
while i < len(floats):
    sumUp += floats[i]
    i += 1

avg = sumUp / len(floats)
print("the average is %s" % str(avg))
