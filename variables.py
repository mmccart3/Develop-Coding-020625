my_name = "Mark McCarthy"
my_age = 60
instructor_status = True

print(my_age)

my_name = input(" Please type your name >")
my_age = input("please type in your age >")

print(my_age)

print(my_name,my_age,instructor_status)

# Cocatentation method but is limited to one type of data - DO NOT USE
print("My name is "+my_name)

#.format() method - DO NOT use
print("My name is {} my age is {}".format(my_name,my_age))

# f string method - use this
print(f"My name is {my_name} and my age is {my_age} and it is {instructor_status} that I am an instructor")