# we can get the length of a string with
print(len("Dogs"))

# But ints have no len()

# Data types in Python:

# String, with some fun slicing
print("North Carolina"[3:14:2])
print("123" + "1718")  # <---- this will just concat

# if you iterate over a string, you can get each char from the str
strIter = "Boo!"
for char in strIter:
    print(char)

# Integer
print(789 + 3)
# we can show large nums with _ instead of , and our machines will ignore them
print(987_000)

# All numbers, + or - all called ints, but if they have a decimal, they are called floats
print(f"I am a float ", 9.88)


# Boolean (True or False)

# Let's do a type converion to change our input int to a str so we can use it
city = input("What is your favorite city? ")
if city:  # Checks if city is not an empty string or None
    name_length = len(city)
    name_length_str = str(name_length)
    print("Your favorite city has " + name_length_str + " letters!")
else:
    print("You didn't enter a city!")

# Here are some fun things with a str and float conversion:
print(str(70) + str(100.0))

# Let's concat the nums and then actually add them to show the difference of what we are doing


def concattyNums(num1, num2):
    return str(num1) + str(num2)


def addedNums(num1, num2):
    return num1 + num2


print(concattyNums(9, 3))
print(addedNums(7, 11))

users_num = input("Enter a number over 10: ")
users_num2 = input("Enter a number over 100: ")

first_digit = int(users_num[0])
second_digit = int(users_num2[1])

print(first_digit + second_digit)

# Do some math with Python
print(3 + 8)
print(8-3)
print(8 * 3)
print(6/3, 'floating point division')
print(9 // 4, 'floor division')
print(2 ** 2)  # <--- exponents are built into the language

# Python uses PEMDAS

# Let's build a BMI Calculator to work on all of these skills
# A BMI is a usrs weight in kg divided by their height squared
weight = input("What is your weight? ")
height = input("Please enter your height in meters. ")
unit = input("Was that lbs or kg? Enter lb or kg please. ")
height = float(height)


def unit_check(weight, unit):
    if unit == "lb":
        weight = float(weight) * 2.2
    elif unit == "kg":
        weight = float(weight)
    return weight


weight_to_calc = unit_check(weight, unit)
bmi_calc = round(weight_to_calc/height**2, 2)


print(f"Your BMI is: " + str(bmi_calc))

# How many weeks of life do we have left?
age = input("How many years old are you? ")
age_in_weeks = int(age) * 52

how_many_left = 4000 - age_in_weeks

print(f"You have {how_many_left} weeks left! Get out there and live!")

# Build a tip calculator
# Welcome the user.
print("Welcome to the tip calculator! ")
# Ask what is the bill total
total = input("What is the total of the bill? ")
total = float(total)
# What is the tip percentage that you want to give. Must be over 15%. Don't be a jerk!
percent = input("What is the percentage you want to tip? Don't be stingy! ")
percent = int(percent)
# How many people are splitting the bill?
guests = input("How many people are splitting the bill? ")
guests = int(guests)
tip = percent/100
total_divided_by_tip = total * tip
total_with_tip_added = total + total_divided_by_tip
total_per_person = round(float(total_with_tip_added/guests), 2)

# Tell the user the amount each person should pay.
print(f"Each guest should pay {total_per_person}")
# or we can format with
# total_per_person = "{:.2f}".format(float(total_with_tip_added/guests))
