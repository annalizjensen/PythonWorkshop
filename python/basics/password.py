"""
Python Workshop: password.py
Anna Jensen, Flipboard, 2017

Demonstrates while loops, continue, and break
"""

correct_user = "Mike"
correct_password = "Awesome!"

while True:
    user = input("Who are you?: ")
    if user != correct_user:
        continue

    password = input("What is your password, Mike?: ")
    if password == correct_password:
        break

print("Access granted!")
