from day16funs import hey
from turtle import Turtle, Screen
tommy = Turtle()

# What is OOP?
# The more complex that our code gets, we need to organize it better so that we don't create spaghetti code.
# The way that we coded our coffee shop was procedural code. It's where procedures of functions lead to the next and the computer jumps around to get what it wants from where it is.
# More complex programs though are super hard to work with when written in procedural code.
# We are going to create a program for a self-driving jet ski.
# What will we ned?
# A camera
# A gps
# A map
# Fuel management
# OOP is splitting a larger task into smaller pieces that are reusable.

# How can we use OOP?
# We can think of using it to model a real world project. Think of what our jet ski has and what it does.

# has:    floats = True        colors = ['blue', 'green', 'white']
# does:     def drive()          def get_gas()

#       an  ATTRIBUTE is what it HAS
#       a METHOD is what it DOES

# An attribute is a variable attached to a particular obj.
# A method is a function that belongs to something.

# In OOP we are modeling real world objects with attributes and methods.
# An obj combines data and functionality.

# We call call the blueprint, or type we created, a class.
# individual items made from the class/blueprint are called objects.
# Let's create some objs with classes
# The obj is the thing we are using in our code
# when creating a new obj from our Class, we must use () on the class name to construct the obj from the blueprint.

tommy.color("blue")
tommy.shape("turtle")
# Drawing a square for visualization
for _ in range(4):
    tommy.forward(100)
    tommy.right(90)

print(hey)
print(tommy)
my_screen = Screen()
# Screen is an obj, canvheight is an attribute on it
print(my_screen.canvheight)
my_screen.exitonclick()
