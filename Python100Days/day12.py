from random import randint
# Let's chat about scope.
# Scope refers to where you can use things in your code.
# Imagine you have a garden, inside your fenced yard. Only your family, inside the fence, can access your garden.
# But in the park next to your house is an apple tree and anyone is welcome to access, or eat, those apples. That's like scope.

friends = 1


def make_new_friends():
    friends = 2
    print(f"Friends from inside the function {friends}")


make_new_friends()
print(f"Friends in the global scope {friends}")


def drink_potion():
    potion_strength = 2
    print(potion_strength)


# We can access the local var by calling the func
drink_potion()
# But we can't just print the local var
# print(potion_strength)  <---Gives a NameError

# When you create a var in a func, you can only use it when you're inside that function bc of local scope.

# Want to access it everywhere? Use global scope?
dog = ["This", "is", "in", "global", "scope", "So we can use it anywhere!"]

# That's the concept of namespace
# When you give a name to a namespace, that namespace is valid in certain scopes.

# Nested funcs have diff var scopes.
# When you create funcs and try to use them, pay attention to where you made them and how the logic works.


def get_scope_info():
    def print_scope_info():
        for item in dog:
            print(item)
    print_scope_info()


print(get_scope_info())

# JS has block scope
# So if we create a new var in an indented block of code, it still has the same scope as the enclosing function.
cats = 3
if cats < 5:
    cat_message = dog[0]

print(cat_message)

# ^^^^^^ If the above was in a func, we couldn't print the message out there. To print it, we'd need to be in the boundaries of the function.

# Vars created in funcs can only be accessed in the func.
# Vars created anywhere else- if block, while loop, for loop, then it does not count as only having local scope.

# We can modify vars that have a global scope.
supplies = ["tent", "chair", "blankets", "lantern"]


def go_camping():
    global supplies
    supplies.append("fishing gear")
    print(f"Supplies from in the camping function {supplies}")


go_camping()
print(f"Supplies from outside of the camping function: {supplies}")

# Set global constant vars with capital letters
PI = 3.14159


def calc():
    print(PI + 3)


calc()

# Let's create a number guessing game.

EASY_LEVEL_TURN_COUNT = 10
HARD_LEVEL_TURN_COUNT = 5
turns = 0


def set_difficulty():
    level = input("Choose a level of difficulty. Type 'easy' or 'hard' ")
    if level == 'easy':
        return EASY_LEVEL_TURN_COUNT
    else:
        return HARD_LEVEL_TURN_COUNT


# Write a function to check user's guess against the number
# We could pass in the global turns here and use it
# But we aren't
# Why?
# Because we don't want to modify the global var of turns. So instead we just pass it in as an arg and then modify that.
def check_answer(guess, answer, turns):
    """Checks the answer against guess and returns the number of turns that remain. """
    if guess > answer:
        print("Too high! ")
        return turns - 1
    elif guess < answer:
        print("Too low! ")
        return turns - 1
    else:
        print(f"You win! The answer was: {answer}")


def guessing_game_play():
    # Choose a random number between 1 and 100
    print("Let's play a number guessing game! ")
    print("Guess a number between 1 and 100: ")
    answer = randint(1, 100)
    print(f"    **********   {answer}  ********")
    # Make a function to set difficulty

    # Track the number of guesses and reduce turns by 1 if they get it wrong

    # Repeat the guessing functionality if they get it wrong.
    guess = 0
    turns = set_difficulty()
    while guess != answer:
        # User needs to guess a number
        guess = int(input("Make a guess: "))
        print(f" You have {turns} attempts left to choose the right number")

        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You have no more guesses, you lose. ")
            return
        elif guess != answer:
            print("Guess again :) ")


guessing_game_play()
