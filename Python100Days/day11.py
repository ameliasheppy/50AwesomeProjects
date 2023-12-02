import random
# Let's make Blackjack!
# Cards in your hand must be 21 or under.
# If over 21, you go bust and lost immediately.
# Cards 2-10 are counted at their face value.
# JQK all count as 10
# Ace is 1 or 11. Depends on what you want the ace to be.
# IF there is a tie with dealer, there is a draw where you each get one more card.
# If the dealer ends up with a hand that is smaller than 17, they must take another card.

# Have the ace count as 11, unless the user goes over 21, then it will be a 1.

# assume that we have an infinite deck - card is drawn === NOT removed from deck. Assume each card has an equal chance of occurring.


def pick_a_card():
    """Returns a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    return random.choice(cards)


def calculate_score(lst):
    """Take in a list of cards and then calculate their total."""
    if sum(lst) == 21 and len(lst) == 2:
        return 0

    if 11 in lst and sum(lst) > 21:
        lst.remove(11)
        lst.append(1)

    return sum(lst)


def compare(user_score, dealer_score):
    if user_score == dealer_score:
        print("Draw!")
    elif dealer_score == 0:
        return "You lost! The user has Blackjack "
    elif user_score == 0:
        return "Blackjack! You win!! :)"
    elif user_score > 21:
        return "You went over 21, you lose :("
    elif dealer_score > 21:
        return "User went over 21, computer wins! "
    elif user_score > dealer_score:
        return "You win!! Computer loses"
    else:
        return "You lose :(  Computer wins"


def play_blackjack():
    user_cards = []
    dealer_cards = []
    is_game_over = False

    # WE MUST APPEND HERE!! Cannot use user_card += new_card bc int is not iterable.
    # += is shorthand for the extend method. Which takes in a list. So what we += must be a list, not a number.

    for _ in range(2):
        user_cards.append(pick_a_card())
        dealer_cards.append(pick_a_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)

        print(f" Your cards: {user_cards}, current score {user_score}")
        print(f" Your cards: {dealer_cards}, current score {dealer_score}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input(
                "Type 'c' to get another card, type 'p' to pass: ")
            if user_should_deal == "c":
                user_cards.append(pick_a_card())
            elif user_should_deal == "p":
                user_cards.append(pick_a_card())
                is_game_over = True
            else:
                print("I didn't understand that command, sorry! ")

    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(pick_a_card())
        dealer_score = calculate_score(dealer_cards)

    print(
        f" Your final hand: {user_cards} and your final score is: {user_score}")
    print(
        f" The computer final hand was {dealer_cards} and the computer's final score is: {dealer_score}")
    print(compare(user_score, dealer_score))


while input("Do you want to play a game, type 'yes' or 'no' ") == "yes":
    play_blackjack()
