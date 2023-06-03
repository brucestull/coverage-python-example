import random

from characters import ALPHABET, NUMBERS


list_of_characters = []

get_in_the_loop = True
if get_in_the_loop:
    list_of_characters.append(random.choice(ALPHABET))

get_in_the_loop = False
if get_in_the_loop:
    list_of_characters.append(random.choice(ALPHABET))
    list_of_characters.append(random.choice(NUMBERS))
    list_of_characters.append(random.choice(ALPHABET))
    list_of_characters.append(random.choice(NUMBERS))
    list_of_characters.append(random.choice(ALPHABET))
    list_of_characters.append(random.choice(NUMBERS))
    list_of_characters.append(random.choice(ALPHABET))
    list_of_characters.append(random.choice(NUMBERS))
    list_of_characters.append(random.choice(ALPHABET))
    list_of_characters.append(random.choice(NUMBERS))
    list_of_characters.append(random.choice(ALPHABET))
    list_of_characters.append(random.choice(NUMBERS))
    list_of_characters.append(random.choice(ALPHABET))
    list_of_characters.append(random.choice(NUMBERS))

print(list_of_characters)
