print("Hello world!")

# Now with a new line after each:
print("Hello World!\nHello World!\nHello World!")

# Or we can print with """"""
print("""
Hello world, 
from 3 different lines 
in my code editor!
""")

# Lets do a concat with a "+"
print("Hello" + " " + "Angela")


# You will get an indentation error if your line has a random space or tab at the beginning!
# Enable syntax highlighting to help with that! I use a rainbow extension

name = input("what is your name? ")
print(f"Welcome {name}!")

# or we could
# print("Hey there " + input("What is your name again? "))


def countTheChars(name):
    return len(name)


print(countTheChars(name))
