# Another handy, but potentially dangerous, loop we can do with Python is a while loop
# When using this type of loop, we can enter an infinite loop if we don't set a condition to exit the loop.

# Imagine if we plug in our Roomba and give it the direction "While you are plugged in, go forward." The Roomba would be able to go forward while it is plugged in. After it goes forward far enough, it will unplug itself, thus ending our command.

# How is this different from a for loop? In a for loop like this:
loop_items = ["Cat", "Dog", "Bunny"]
for item in loop_items:
    print(item)
# We are doing something with each item. And with a range of nums, we can do something to each number, like multiply or print.
for number in range(1, 5):
    print(number ** 2)

# The while loop meanwhile, runs on a truthy condition. It does an action repeatedly only while the condition is true.
number_while = 6
while number_while < 10:
    number_while += 1
    print(number_while)
