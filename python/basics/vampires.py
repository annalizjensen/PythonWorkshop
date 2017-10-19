"""
Python Workshop: vampires.py
Anna Jensen, Flipboard, 2017

Demonstrates boolean logic and control flow
"""

name = input("What is your name?: ")
age = input("What is your age?: ")
topic = input("What is your favorite topic?: ")
muted = input("What source have you muted?: ")

if int(age) >= 120 or topic == "Nocturnal" or muted == "Garlic Monthly":
    print(name + " is a vampire!")
else:
    print(name + " is not a vampire.")
