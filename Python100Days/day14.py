from day14data import data
import random


def format(account):
    """ Format the account data into printable format"""
    account_name = account["name"]
    account_description = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_description}, from {account_country}"


def check_answer(guess, a_followers, b_followers):
    """Use an if statement to check if the user is correct"""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


# Generate a random account from the game data
score = 0
game_should_continue = True
account_b = random.choice(data)
# Make the game repeatable

while game_should_continue:
    account_a = account_b
    account_b = random.choice(data)

    while account_a == account_b:
        account_b = random.choice(data)

    print(f"Compare A: {format(account_a)} against B: {format(account_b)}")

    # Ask user for a guess
    guess = input("Who has more followers? Type 'a' or 'b'").lower()

    # Get follower count of each account
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    # Use if statement to check if user is correct
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    # Give user feedback on their guess
    if is_correct:
        # Keep score
        score += 1
        print(f"You're right! Current score: {score}")
    else:
        game_should_continue = False
        print(f"Sorry, wrong guess. Final score: {score}")
