# We need to add some randomness to our programs at times.

# Computers are deterministic. A bunch of math can be applied to create random programs.

# Go watch the Khan Academy videro about pseudo random number generators.

# We can go to AskPython.com to learn fun modules and stuff we can use

import day4_module
import random

# We can generate a random number with randint from the random module. Modules are chunks of code responsible for various tasks. With an airplane, imagine a wing module, a landing gear module, a windows module.

random_num = random.randint(1, 130)
print(random_num)
random_float = random.random()
print(random_float)
random_float_up_to_five = (random.random()) * 5
print(random_float_up_to_five)

# Let's build a quick coin flip program to tell the user what they got

if random_float >= 0.5:
    print("Heads!")
else:
    print("Tails!")


# Can we make our own modules? Yes! We can make one we will call dogs.

print(day4_module.dogs)
print(day4_module.dogs)
print(day4_module.dogs[1])

# Bam! We just printed off a list of dogs from the dogs module. We will use Python lists constantly. We can store our data in related collections that are ordered. We can access these lists of same or different data types by their index. Order is determined by where the item is in the list.

# We can add things or remove things to the list in different ways.

day4_module.dogs.append("Winnie")
day4_module.dogs.append("Tank")
day4_module.dogs.append("Tink")
day4_module.dogs.extend(["Sheldon", "Smarty", "Nick Miller"])

print(day4_module.dogs)

# Go to docs.python.org/3/ for more info and search topics that we want to learn about

# We are heading off for a fun beach vacation, but we can only take one of the dogs! Pick one with random.

dog_list = day4_module.dogs

# Let's generate a random index from our list:

random_dog = random.randint(0, len(dog_list) - 1)

vacation_buddy = dog_list[random_dog]
print(f"Pack the collar, leash and bowl for {vacation_buddy}")

# When we work with lists, we come across the index out of range area. Why? It means that we are trying to access an index that does not exist! It's like an off by one error. We have 10 items, want to reach the 10th item, so access the 10th item in the list, you'd use dogs[9] instead of dogs[10]. This is due to the off-by-one error, where attempting to access dogs[10] would exceed the list's bounds and result in an 'index out of range' error. Therefore, to access the 10th item in the list, you'd actually reference it as dogs[9] to correctly fetch the last item in a list of length 10. And if we don't know the length of the list, we can do the below.
last_dog = dog_list[len(dog_list) - 1]
# We can work with nested lists too

cats = ["Tom", "Jerry", "Pickle"]
pets = [dog_list, cats]
print(pets)
