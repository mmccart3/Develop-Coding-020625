# import random #This method is more verbose
from random import random, randint, choice # This method is more memory efficient
from time import sleep
from openpyxl import Workbook
print(random())
sleep(0.5)
print(randint(1,100))
sleep(0.5)
my_list = ["dragon","orc","goblin","hobbits", "ogre", "troll", "fairy"]
print(choice(my_list))
sleep(0.5)
my_string = "The quick brown fox jumps"
# for each_letter in my_string:
#     print(each_letter)
#     sleep(0.1)
# my_string = "over the lazy dog"
for each_letter in my_string:
    print(each_letter)
    sleep(0.1)
for number in range (1,11):
    sleep(0.1)
    print(number)
