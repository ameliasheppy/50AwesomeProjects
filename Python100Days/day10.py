# Let's make a function that gives capitalization to names

def capitalize(first, last):
    first = first.title()
    last = last.title()
    return (f"{first} {last}")


print(capitalize("amy", "stanley"))

# Let's make a months function that will take in a year and a month and tell you how many days are in the month.


def is_leap_year(year_to_check):
    if year_to_check % 4 == 0:
        if year_to_check % 100 == 0:
            if year_to_check % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


def days_in_month(year, month):
    days_per_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if month == 2 and is_leap_year(year):
        return 29

    else:
        return days_per_month[month-1]


year = int(input("Enter a year "))
month = int(input("Enter a month "))
days = days_in_month(year, month)
print(days)

# I am going to write a function that will return proper casing for a name, no matter what the user enters as input
badly_typed_noun = input(
    "Please enter your name, but ignore capitalization rules   \n")


def fix_the_spongebob_text(name):
    edited = []
    for letter in name:
        if letter == name[0]:
            edited.append(letter.title())
        else:
            edited.append(letter.lower())

    return ''.join(edited)


print(fix_the_spongebob_text(badly_typed_noun))


def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    return num1 / num2


operations = {"+": add, "-": subtract, "x": multiply, "/": divide}


def my_calculator():
    for symbol in operations:
        print(symbol)

    more_calculations = True

    number1 = float(input("First number: "))
    while more_calculations:
        number2 = float(input("Next number: "))
        user_operation = input("Pick an operation from the list above: ")
        calculations = operations[user_operation]
        answer = calculations(number1, number2)

        print(f"{number1} {user_operation} {number2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to exit. ") == "y":
            number1 = answer
        else:
            more_calculations = False
            return


my_calculator()
