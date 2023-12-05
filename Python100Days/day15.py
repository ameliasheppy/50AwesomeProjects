# Let's open a coffee shop. Here is our menu for hot espresso drinks
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def can_we_make_that_coffee(current_stock):
    for item in current_stock:
        if current_stock[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def count_the_coins():
    """Returns the total calculated from coins paid"""
    print("Please insert coins. ")
    # Thei first total below sets the var, the rest inc it
    total = int(input("How many quarters: ")) * 0.25
    total += int(input("How many dimes: ")) * 0.10
    total += int(input("How many nickles: ")) * 0.05
    total += int(input("How many pennies: ")) * 0.01
    return total


def is_transaction_successful(monies, drink_cost):
    """Return True if amount is enough to cover the cost. False if insufficient funds"""
    if monies > drink_cost:
        change = round(monies - drink_cost, 2)
        print(f"Here is your change {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money")
        return False


def make_the_coffee(drink_name, ingredients_to_decrement):
    """Deduct the required ingredients from the resources """
    for item in ingredients_to_decrement:
        resources[item] -= ingredients_to_decrement[item]
    print(f"Here is your {drink_name}")

# Our espresso machine should:
# Print a status report of what quantities are left of ingredients
# Alert when insufficien ingredients for different drinks, and offer refunds to the user if needed.
# Process coins
# Check if the transaction was successful
# Make the coffee for the user and update status/earned money


is_on = True
while is_on:
    order = input(
        "What would you like to order? (cappucino latte or espresso) \n")
    if order == "off":
        is_on = False
    elif order == "report":
        print(f"Water: {resources['water']}mL,")
        print(f"Milk: {resources['milk']}mL,")
        print(f"Coffee: {resources['coffee']}g,")
        print(f"Money: {profit}")
    else:
        customer_choice = MENU[order]
        if can_we_make_that_coffee(customer_choice["ingredients"]):
            payment = count_the_coins()
            if is_transaction_successful(payment, customer_choice["cost"]):
                make_the_coffee(order, customer_choice["ingredients"])
