from random import randint

random_number = randint(1,100)

def make_guess():
    global random_number
    user_guess = int(input("Please enter a guess between 1 and 100 >"))
    if user_guess == random_number:
        print(f"{user_guess} is the correct answer {random_number}")
    else:
        if user_guess > random_number:
            print("Too High")
        else:
            print("Too Low")
        make_guess()

make_guess()