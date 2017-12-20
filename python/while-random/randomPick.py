from random import *

while True:
    choices = [0,1,2,3]
    print("choose:")
    print("0 - quit")
    print("1 - flip a coin")
    print("2 - roll a die")
    print("3 - pick a number between 1 - 10")
    choice = int(input("what is your choice? "))

    if choice not in choices:
        print("That's not an acceptable choice")
        continue

    if choice == 0:
        break
    else:
        if choice == 1:
            result = randrange(0,2)
            if result== 0:
                string = "heads"
            else:
                string = "tails"
            print("Result is %s" %string)
        elif choice == 2:
            result = randrange(0,6)
            print("Result is %d" %(result + 1))
        else:
            result = randrange(0,10)
            print("Result is %d" %(result + 1))
