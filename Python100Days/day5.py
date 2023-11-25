import random
import string
# https://haveibeenpwned.com/

# Let's build a password generator! (Just for fun! You clone or fork this repo-> know that this is all for funs, I'm not a security expert! )


print("Welcome to the Really Handy Dandy Password Generator!")


def generate_password(letters_count, symbols_count, numbers_count):
    letters = ''.join(random.choice(string.ascii_letters)
                      for _ in range(letters_count))
    symbols = ''.join(random.choice("!*&#$?#+>") for _ in range(symbols_count))
    numbers = ''.join(random.choice(string.digits)
                      for _ in range(numbers_count))

    password = letters + symbols + numbers
    password_list = list(password)
    random.shuffle(password_list)

    return ''.join(password_list)


num_letters = int(input("How many letters would you like in your password? "))
num_symbols = int(input("How many symbols would you like in your password? "))
num_numbers = int(input("How many numbers would you like in your password? "))

new_password = generate_password(num_letters, num_symbols, num_numbers)
print("Here is your fancy new secure password: ", new_password)


# Python loops are great. Think of something that we want to happen over and over, and then use a loop to accomplish it! We can rewrite that using loops and not using the string module:


def generate_password(letters_count, symbols_count, numbers_count):
    password = ''

    # Generate letters (uppercase and lowercase)
    for _ in range(letters_count):
        # Uppercase letters (ASCII 65-90)
        password += chr(random.randint(65, 90))
        # Lowercase letters (ASCII 97-122)
        password += chr(random.randint(97, 122))

    # Generate symbols
    symbol_set = "!*&#$?#+>"
    for _ in range(symbols_count):
        password += random.choice(symbol_set)

    # Generate numbers
    for _ in range(numbers_count):
        password += chr(random.randint(48, 57))  # Digits (ASCII 48-57)

    # Shuffle the password characters
    password_list = list(password)
    random.shuffle(password_list)

    return ''.join(password_list)


num_letters = int(input("How many letters would you like in your password? "))
num_symbols = int(input("How many symbols would you like in your password? "))
num_numbers = int(input("How many numbers would you like in your password? "))

new_password = generate_password(num_letters, num_symbols, num_numbers)
print("Here is your fancy new secure password:", new_password)


# Want to print a list of items?

items = ["Leash", "Collar", "Water and food bowls",
         "Toys", "Nylabones", "Puppy kibbles"]

for item in items:
    print(item)

# Want the items and their index, so we have a handy list?
# Remember, CS starts with 0, so add one to the starting index.

for idx, item in enumerate(items):
    print(f"{idx +1}. {item}")


# Let's write a small program using loops to calculate the average score of students on a test.

student_scores = [98, 71, 93, 89, 100, 80, 92, 92, 87]

class_total = 0
for score in student_scores:
    class_total += score

print(class_total)
print(
    f"The average score this test was {round(class_total/len(student_scores), 1)}")

# Let's also compute which student had the highest score, bascially replicating the max method with Python.

highest = 0
for score in student_scores:
    if score > highest:
        highest = score
print(highest)

# Think about Python loops.
# Loop through a list, we get back each item from a list
# Loop through  a string, get back each char from the string
# Loop through a file, we can get back each line from the file
# Numbers, like integers and floats, are not iterable. We can't iterate through each individual digit or part of a number. But we can use loops to iterate over a range of numbers or create a sequence of numbers.

for i in range(5):
    print(i)

# Above we are printing the range 0-4. Range is not inclusive of th high number that we use in it.

# Python loops are wonderfully flexible and we can use them to iterate over various types of DS.

# Carl Gauss figured out a BOSSSSSS way to iterate over numbers.
# This does not require looping over in many iterations:


def gauss_sum(n):
    return (n * (n + 1)) // 2


gauss_result = gauss_sum(100)
print(gauss_result, "  <---- Done with Gauss's awesome trick!")

# We can also do fun steps with range:
for number in range(200, 303, 25):
    print(f"Here is your {number}")


# Let's write a simple program. We want to calculate the sum of the odd numbers from one to X. If X is 100, then the first odd number is 1 and the last one is 99.
# Only take inputs up to 500
target = int(input("What number shall we get use up to 500?    "))
target_total_odds = 0
target_total_all = 0
for number in range(0, target + 1):
    if number % 2 == 1:
        target_total_odds += number
print(target_total_odds)

for number in range(0, target):
    target_total_all += number
print(target_total_all)

# FizzBuzz interview question


def fizzbuzz(num):
    for number in range(1, num + 1):
        if number % 3 == 0 and number % 5 == 0:
            print("FizzBuzz")
        elif number % 3 == 0:
            print("Fizz")
        elif number % 5 == 0:
            print("Buzz")
        else:
            print(number)


(fizzbuzz(15))

# FizzBuzz Interview question from Shipt:


def fizz_buzz_shipt(num):
    f_b_arr = []

    for number in range(1, num + 1):
        if number % 3 == 0 and number % 5 == 0:
            f_b_arr.append("FizzBuzz")
        elif number % 3 == 0:
            f_b_arr.append("Fizz")
        elif number % 5 == 0:
            f_b_arr.append("Buzz")
        else:
            f_b_arr.append(str(number))
    return f_b_arr


print(fizz_buzz_shipt(90))
