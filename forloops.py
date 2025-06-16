# for index in range(10):
#     print(index)

# for index in range (1,11):
#     print(index)

# for index in range (2, 101, 2):
#     print(index)

my_tunes = [
    'Zoom',
    'Bohemian Rhapsody',
    'Stairway to Heaven',
    'American Pie'
]

# for index in range(len(my_tunes)):
#     print(my_tunes[index])
# for each_tune in my_tunes:
#     print(each_tune)

# def film_check(film_to_checked):
#     if film_to_checked.lower() == "ghostbusters":
#         print(film_to_checked, " - yay it's Ghostbusters")
#     else:
#         print(film_to_checked, " - oh no I want Ghostbusters")

# list_of_films = [
#     'The Shawshank Redemption',
#     'Crimson Tide',
#     "It's a Wonderful Life",
#     'Ghostbusters'
# ]

# for each_film in list_of_films:
#     film_check(each_film)

# for i in range(10):
#     print(i)

# from time import sleep
# for i in range(9,-1,-1):
#     sleep(1)
#     print(i)

# from random import randint

# target_number = randint(1,100)
# print(f"Target number is {target_number}")

# guessed_number = randint(1,100)
# counter = 1
# while guessed_number != target_number:
#     print(f"{counter} guessed_number is {guessed_number}")
#     guessed_number = randint(1,100)
#     counter += 1

# def get_user_direction():
#     user_input = input("Please enter N to go North, S to go South, E to go East, W to go west >").lower()
#     print(f"user input = {user_input}")

#     while user_input != 'n' and user_input != 's' and user_input != 'e' and user_input != 'w':
#         user_input = input("Please enter N to go North, S to go South, E to go East, W to go west >").lower()
#         print(f"user input = {user_input}")
#     return user_input

# user_direction = get_user_direction()
# print(user_direction)

# # Challenge 3
# table = int(input("Which times-tables do you wish to see? "))

# for index in range (1,13):
#     print(f"{index} x {table} = {index*table}")

#Challenge 4
list_of_primes =[]
for number in range (2,101):
    is_prime = True
    for index in range (2,number):
        if number % index == 0:
            is_prime = False
    if is_prime:
        list_of_primes.append(number)
print(list_of_primes)        