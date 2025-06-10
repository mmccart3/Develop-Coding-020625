# music_selection = input("What type of music would you like to listen to? >").lower()

# if music_selection == "classical":
#     print("I hate classical music, please turn it off!")
# elif music_selection == "rock":
#     print("That's OK let's listen")
# elif music_selection == "dance":
#     print("I love it! Turn it right up!")
# elif music_selection == "80s":
#     print("OK. Go with it")
# elif music_selection == "modern classical":
#     print("groovy baby!")
# else:
#     print("Sorry I don't recognise that music")

age = int(input("What is your age? >"))
country = input("Which country are you in US or UK").upper()

if (age > 17 and country == "UK") or (age > 20 and country == "US"):
    print("welcome would you like to drink")
else:
    print("you are too young, get out")