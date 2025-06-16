# # Dictionaries are similar to objects in other languages.

# mark = {
#     'key'        : 'value',
#     'first_name' : 'Mark',
#     'last_name'  : 'McCarthy',
#     'age': 60,
#     'eye_colour' : 'blue'
# }

# print(mark['eye_colour'])

character1 = {
    'race': 'ogre',
    'class': 'knight',
    'attacking_strength': 70,
    'defensive_strength': 52
}
# print(character1.values())
character2 = {
    'race': 'hobbit',
    'class': 'knight',
    'attacking_strength': 30,
    'defensive_strength': 48
}
character3 = {
    'race': 'elf',
    'class': 'king',
    'attacking_strength': 80,
    'defensive_strength': 100
}

list_of_characters = [
    character1,
    character2,
    character3
]

# print(list_of_characters)
# print(list_of_characters[-1]['race'])

# print(list_of_characters[0])
# print(list_of_characters[1])
# print(list_of_characters[2])

for character in list_of_characters:
    print(character['race'],'\t',character['class'],'\t',character['attacking_strength'],'\t',character['attacking_strength'])