"""
vowels.py
"""
from random import *

"""
part one - replace vowels
"""
vowels = ["a", "e", "i", "o", "u"]
user_input = input("Please enter a string: ")
character = input("Please enter a character replacement: ")

result = ""
for letter in user_input.lower():
    if (letter in vowels):
        result += character
    else:
        result += letter

print("Resulting string " + result)

"""
part two - replace vowels with random vowels
"""

# check whether the string contains any vowels
if not any(char in vowels for char in user_input.lower()):
    print(user_input)
    print("Your string contains no vowels.")

else:
    result = ""
    for letter in user_input.lower():
        if letter in vowels:
            vowel = choice(vowels)
            # if it's the same vowel, we have to keep picking until it's not
            while vowel == letter:
                vowel = choice(vowels)
            # once it's not the same, we're good
            result += vowel
        else:
            result += letter

    print("Your new string is: " + result)

"""
part three - case sensitive replacement
"""
upper_vowels = ["A", "E", "I", "O", "U"]
lower_vowels = vowels


if not any(char in vowels for char in user_input.lower()):
    print(user_input)
    print("Your string contains no vowels.")

else:
    result = ""
    for letter in user_input:
        if letter in upper_vowels:
            vowel = choice(upper_vowels)
            while vowel == letter:
                vowel = choice(upper_vowels)
            result += vowel
        elif letter in lower_vowels:
            vowel = choice(lower_vowels)
            while vowel == letter:
                vowel = choice(lower_vowels)
            result += vowel
        else:
            result += letter

    print("Your final result is " + result)
