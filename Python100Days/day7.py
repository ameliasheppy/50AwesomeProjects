import random
from day7stages import stages
from day7words import words

word_to_guess = random.choice(words)
print(word_to_guess)

word_progress = ['_'] * len(word_to_guess)
guessed_letters = []


def hangman():
    global word_progress
    global guessed_letters
    max_attempts = 6
    while "_" in word_progress and max_attempts > 0:
        guess_by_user = input(
            "Guess a letter from the animal name clue please: ").lower()

        if guess_by_user in guessed_letters:
            print("You've already guessed that letter. Try another one.")
            continue

        guessed_letters.append(guess_by_user)

        if guess_by_user in word_to_guess:
            for i in range(len(word_to_guess)):
                if word_to_guess[i] == guess_by_user:
                    word_progress[i] = guess_by_user

            print(f"Good guess! Progress: {''.join(word_progress)}")
        else:
            max_attempts -= 1
            print(stages[max_attempts])
            print(f"Wrong guess! Attempts left: {max_attempts}")

    if "_" not in word_progress:
        print(f"Congratulations! You've guessed {word_to_guess}!")
    else:
        print(f"Oops! The word was '{word_to_guess}'. Better luck next time!")


hangman()


# We could also do this
for position in range(len("North Carolina")):
    print(position ** 2)

# OR:
for idx, item in enumerate(range(len("NagsHead"))):
    print(f"Letter {idx +1}: {item}")
