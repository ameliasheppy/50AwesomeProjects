# Now with a new line after each:
print("Hello World!\nHello World!\nHello World!")

# Or we can print with """"""
print("""
Hello world, 
from 3 different lines 
in my code editor!
""")

# Lets do a concat with a "+"
print("Hello" + " " + "Amelia")


# You will get an indentation error if your line has a random space or tab at the beginning!
# Enable syntax highlighting to help with that! I use a rainbow extension

name = input("what is your name? ")
print(f"Welcome {name}!")

# Or we could
# print("Hey there " + input("What is your name again? "))


def countTheChars(name):
    return len(name)


print(countTheChars(name))

# Let's work on changing some vars!
a = input("Type a number: ")
b = input("Type another number: ")

print("a: " + str(b))
print("b: " + str(a))

# We can't use python's reserved words as var names!
# Check the list of Python's keywords to make sure that we don't.

# Assignment #1
# Lizard Name Generator:

# 1. Create a greeting for your program
print("Welcome! What should you name your new lizard? Answer the next questions to find out!")
# 2. Ask the user for a favorite city
city = input("What's your favorite city? ")
# 3. Ask the user for the name of a pet.
street = input("What is the name of your favorite street? ")
# 4. Combine the name of their city and pet and show them their band name.
print(f"Congrats on getting {city} {street}!!")
# 5. Make sure that the program completes with no errors!
