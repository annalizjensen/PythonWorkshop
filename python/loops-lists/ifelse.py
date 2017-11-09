# Python Course
# Conditionals

# patrons age:
age = 16

# for the US:

if age < 21:
    print("No booz for you!")
    print("How about an Arnold Palmer?")
else:
    print("It's happy hour!")
    print("What'll it be?")


# Canada:
province = "BC"

if province == "AB" or province == "MB" or province == "QC":
    if age < 18:
        print("No booz for you!")
        print("How about an Arnold Palmer?")
    else:
        print("It's happy hour!")
        print("What'll it be?")
elif age < 19:
    print("No booz for you!")
    print("How about an Arnold Palmer?")
else:
    print("It's happy hour!")
    print("What'll it be?")
