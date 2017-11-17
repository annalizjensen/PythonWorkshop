'''
Random raffle winners
Anna Jensen - 11/2017
'''
import random

# asks for and creates list of people
people = []
while True:
    person = input("What is your name? (Or enter 0 if all names entered): ")
    if "0" == person:
        break
    people += [person]

# prints out list to confirm
print("We've collected all the names. Here they are: ")
index = 0 # index from 0!!
while index < len(people):
    print(people[index])
    index += 1 # increment this so we know which name we're on

# asks how many winners (and checks that that is equal to or less than length of list)
winners = input("How many laptops will be raffled off? ")

# randomly selects winner (and waits to continue)
winners = int(winners) # winners must be an int for the while loop
picked = 0
while picked < winners:
    people_length = len(people)
    winner_index = random.randrange(0, people_length)
    print(people[winner_index] + " is a winner!")
    del people[winner_index]
    picked += 1

# exits gracefully
print("All done! Thanks for playing!")
