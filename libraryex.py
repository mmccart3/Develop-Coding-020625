from random import randint

random_number = randint(1,100)

already_correct = False

print("Guess 1")
user_guess = int(input("Please enter a gues between 1 and 100 >"))
if user_guess == random_number:
    print(f"{user_guess} is the correct answer {random_number}")
    already_correct = True
else:
    if user_guess > random_number:
        print("Too High")
    else:
        print("Too Low")

print("Guess 2")
if already_correct == False:
    user_guess = int(input("Please enter a gues between 1 and 100 >"))
    if user_guess == random_number:
        print(f"{user_guess} is the correct answer {random_number}")
        already_correct = True
    else:
        if user_guess > random_number:
            print("Too High")
        else:
            print("Too Low")

print("Guess 3")
if already_correct == False:
    user_guess = int(input("Please enter a gues between 1 and 100 >"))
    if user_guess == random_number:
        print(f"{user_guess} is the correct answer {random_number}")
        already_correct = True
    else:
        if user_guess > random_number:
            print("Too High")
        else:
            print("Too Low")

print("Guess 4")
if already_correct == False:
    user_guess = int(input("Please enter a gues between 1 and 100 >"))
    if user_guess == random_number:
        print(f"{user_guess} is the correct answer {random_number}")
        already_correct = True
    else:
        if user_guess > random_number:
            print("Too High")
        else:
            print("Too Low")

print("Guess 5")
if already_correct == False:
    user_guess = int(input("Please enter a gues between 1 and 100 >"))
    if user_guess == random_number:
        print(f"{user_guess} is the correct answer {random_number}")
        already_correct = True
    else:
        if user_guess > random_number:
            print("Too High")
        else:
            print("Too Low")

print("Guess 6")
if already_correct == False:
    user_guess = int(input("Please enter a gues between 1 and 100 >"))
    if user_guess == random_number:
        print(f"{user_guess} is the correct answer {random_number}")
        already_correct = True
    else:
        if user_guess > random_number:
            print("Too High")
        else:
            print("Too Low")

print("Guess 7")
if already_correct == False:
    user_guess = int(input("Please enter a gues between 1 and 100 >"))
    if user_guess == random_number:
        print(f"{user_guess} is the correct answer {random_number}")
        already_correct = True
    else:
        if user_guess > random_number:
            print("Too High")
        else:
            print("Too Low")

print("Guess 8")
if already_correct == False:
    user_guess = int(input("Please enter a gues between 1 and 100 >"))
    if user_guess == random_number:
        print(f"{user_guess} is the correct answer {random_number}")
        already_correct = True
    else:
        if user_guess > random_number:
            print("Too High")
        else:
            print("Too Low")