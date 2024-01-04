import calendar
import random

# Show a calendar with calendar that we imported
# year = int(input("Enter year: "))
# month = int(input("Enter month: "))
# cal_to_show = calendar.month(year, month)
# print(cal_to_show)

# Find the base of a triangle with Py:
# base = float(input("What is the length of the base of the triangle? "))
# height = float(input("What is the height of the triangle? "))
# area = 0.5 * base * height
# print(f"The area of your triangle is {area}")

# Write a Py program to swap two vars
a = input("Enter the value of the first variable (a): ")
b = input("Enter the value of the second variable (b): ")
print(f"Your original values: a = {a}, b = {b}")
# Swap out the values with a temporary var:
temp = a
a = b
b = temp
print(f" The swapped variables: a = {a}, b = {b}")

# Write a Py program to generate a random number:
print(f"Here is your random number: {random.randint(1,75)}")

# 1 km = 0.621371 miles
# Convert km to miles:
# kilometers = float(input("Enter distance in kilometers:   "))
# conversion_number = 0.621371
# miles = kilometers * conversion_number
# print(f"{kilometers} is equal to {miles} miles. ")

# Convert Celsius to Fahrenheit
# celsius = float(input("What is your Celsius temperature? "))
# fahrenheit = (celsius * 9/5) + 32
# print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit. :) ")

# How can we swap two vars without temp vars
five = 5
ten = 10
five, ten = ten, five
print(f"After the swap: five = {five}, ten = {ten} ")

# Write a program to see if a number is positive, negative or zero
number_to_check = float(input("Enter a number:  "))
if number_to_check > 0:
    print(f"{number_to_check} is positive")
elif number_to_check == 0:
    print(f"{number_to_check} is zero!")
else:
    print(f"{number_to_check} must be negative then. ")

# Let's check to see if a number is prime.
# For this to be true, it must only be divisible by 1 and itself.
is_number_prime = int(input("Enter a number to check if prime: "))
found = False
if is_number_prime == 2:
    found = True
elif is_number_prime > 2:
    for i in range(2, is_number_prime):
        if (is_number_prime % i) == 0:
            found = False
            break
    else:
        found = True
if found:
    print(f"{is_number_prime} is a prime number. ")
else:
    print(f"{is_number_prime} is not a prime number.")

# Print all prime numbers in an interval of 1-10
lower_number = 1
upper_number = 10
print("Prime numbers between ", lower_number, " and ", upper_number, "are: ")
for num in range(lower_number, upper_number + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)

# Find the factorial of a number
num_for_factorial = int(input("Enter a number:  "))
factorial = 1
if num_for_factorial < 0:
    print("Factorials don't exist for negative numbers ")
elif num_for_factorial == 0:
    print("Factorial of 0 is 1. ")
else:
    for i in range(1, num_for_factorial+1):
        factorial = factorial*i
    print(f"The factorial of {num_for_factorial} is {factorial}")


# Display a multiplication table
num_for_mult_table = int(input("Display the multiplication table of: "))
for i in range(1, 11):
    print(f"{num_for_mult_table} X {i} = {num_for_mult_table*i}")

# Use Python to print a Fibonacci sequence (a series of nums where each num is the sum of the two preceding ones, usually starting with 0 and 1.)
number_of_terms = 10
n1, n2 = 0, 1
count = 0
# If accepting input, can check to see if the number of terms is valid
print("Here is our Fibonacci sequence: ")
while count < number_of_terms:
    print(n1)
    nth = n1 + n2
    print(f"{n1} is now and {n2} is now and {nth} is nth")
    n1 = n2
    n2 = nth
    count += 1
