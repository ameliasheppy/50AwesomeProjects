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

# Let's work on making a game that needs user input. Our dog has a bone that they need to bury. Where should they put it?

front_yard = [" ", " ", " "]
garden = [" ", " ", " "]
back_yard = [" ", " ", " "]

holes = [front_yard, garden, back_yard]

print("Bury the dog bone! A mound of dirt in an \"X\" marks the spot. ")
hole = input("Where did the dog bury its snack? Enter a number from 1-9. ")

# we can't use replace here bc we can't modify a str in place, so we need to just reassign the value at the index to x
hole = int(hole)
if hole == 1:
    front_yard[0] = "X"
elif hole == 2:
    front_yard[1] = "X"
elif hole == 3:
    front_yard[2] = "X"
elif hole == 4:
    garden[0] = "X"
elif hole == 5:
    garden[1] = "X"
elif hole == 6:
    garden[2] = "X"
elif hole == 7:
    back_yard[0] = "X"
elif hole == 8:
    back_yard[1] = "X"
elif hole == 9:
    back_yard[2] = "X"
else:
    print("Sorry, please enter a number with a value of 1-9.")

print(f"{front_yard}\n{garden}\n{back_yard}")


# An alternate way to do this is:

line1 = [" ", " ", " "]
line2 = [" ", " ", " "]
line3 = [" ", " ", " "]

# this is a list
map = [line1, line2, line3]
position = input("Type a b or c and a number 1-3 to place your treasure! ")

# make all the letters consistently small
letter = position[0].lower()
abc = ["a", "b", "c"]

# set the letter index to add to our list of lists, map
letter_index = abc.index(letter)
# set the number index to add to our map
number_index = int(position[1]) - 1
# replace the item at the specified index with an x
map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}")

rock = "🪨"
paper = "📃"
scissors = "✂️"

computer_choice = random.choice([rock, paper, scissors])
player_choice = input("rock, paper, or scissors?")
if player_choice == "rock":
    player_choice = rock
elif player_choice == "paper":
    player_choice = paper
elif player_choice == "scissors":
    player_choice = scissors
else:
    print("Try typing your answer again")

winner = ""
if computer_choice == rock and player_choice == scissors:
    winner = "Computer!"
elif player_choice == rock and computer_choice == scissors:
    winner = "you! Great job!"
elif computer_choice == scissors and player_choice == paper:
    winner = "Computer!"
elif player_choice == scissors and computer_choice == paper:
    winner = "you! Great job!"
elif computer_choice == paper and player_choice == rock:
    winner = "Computer! "
elif player_choice == paper and computer_choice == rock:
    winner = "you! Great job!"
else:
    winner = f"no one! You both chose {player_choice}"

print(
    f"Computer's choice is {computer_choice}, player's choice is {player_choice}. Winner is {winner}")
