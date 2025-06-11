# Challenge 1
# 

#Challenge 2
# num = int(input("Please enter the number to be checked >"))

# is_divisble_by_3 = (num % 3 == 0)
# is_divisble_by_5 = (num % 5 == 0)

# if is_divisble_by_3 or is_divisble_by_5:
#     print("This number is divisble by 3 or 5")
# else:
#     print("This number is not divisble by either 3 or 5")

# if (num % 3 == 0) or (num % 5 == 0):
#     print("This number is divisble by 3 or 5")
# else:
#     print("This number is not divisble by either 3 or 5")

# Challenge 3
# num = int(input("Please enter the number to be checked >"))

# if (num % 3 == 0) and (num % 7 ==0):
#     print("Fizz Buzz")
# elif (num % 3 == 0):
#     print("Fizz")
# elif (num % 7 == 0):
#     print("Buzz")
# else:
#     print(num)

# Challenge 4
# word = input("Please enter the word to be checked >").lower()

# if word[0] == word[-1]:
#     print("True")
# else:
#     print("False")

# Challenge 6
# num1 = int(input("Please enter the first number to be checked >"))
# num2 = int(input("Please enter the second number to be checked >"))

# if (num1+num2) % 2 == 0:
#     print("Success")
# else:
#     print("Failure")

#Challenge 7:
num = input("Please enter the number to be checked >")

if num == num[::-1]:
    print("palindrome")
else:
    print("not a palindrome")