# conditionals, logical operators, code blocks and scope
kayak_speed = 12
if kayak_speed > 15:
    print("You win!!")
else:
    print("Paddle faster!")

# Use if and else statements to allow our code to do things based on different circumstances
print("Welcome to our water park!")
height = int(input("How tall are you in inches? "))

if height > 52:
    print("You can go off the high dive :) ")
else:
    print("Sorry, stick to the slides until you are taller please")

# Tell a user if their car was made in an even or odd year
model_year = int(input("What 4 digit year was your car made in? "))


def even_or_odd_year(year):
    if year % 2 == 0:
        print(f"Your car was made in an even year, {year}")
    else:
        print(f"Your car was made in an odd year, {year}")


even_or_odd_year(model_year)

print("Welcome to the fair! Let's get your tickets sorted out.")
fair_height = int(input("How many inches tall are you? "))
fair_age = int(input("How many years old are you? "))
if fair_height > 49:
    print("Okay, let's see what ride category you are in.")
    if fair_age < 12:
        print("Please pay $7 and head to the Green Rides Section")
    elif fair_age <= 18:
        print("Please pay $10 and ride any rides in the Green or Blue Section")
    else:
        print("Please pay $12 and you can ride any ride outside of the Kiddie Zone")

else:
    print("Go ahead and enter the Kiddie Zone!")


# Let's make a BMI that gives the user feedback to see what category their BMI is in.
weight = input("What is your weight? ")
height = input("Please enter your height in meters. ")
unit = input("Was that lbs or kg? Enter lb or kg please. ")
height = float(height)


def unit_check(weight, unit):
    if unit == "lb":
        weight = float(weight) * 2.2
    elif unit == "kg":
        weight = float(weight)
    return weight


weight_to_calc = unit_check(weight, unit)
bmi_calc = round(weight_to_calc/height**2, 2)

if bmi_calc < 25:
    print("Your BMI is less than 25 ")
elif bmi_calc <= 30:
    print("Your BMI is between 25 and 30")
else:
    print("Your BMI is over 30")

print(f"Your BMI is: " + str(bmi_calc))

# Create a program to see if a year is a leap year.
year_to_check = input("What year are you enquiring about? ")


def is_year_a_leap_year(yr):
    if (yr % 4 == 0 and yr % 100 != 0) or (yr % 400 == 0):
        print(f"{yr} is a leap year!")

    else:
        print(f"{yr} is not a leap year")


is_year_a_leap_year(int(year_to_check))
is_year_a_leap_year(1971)
is_year_a_leap_year(2100)

year_to_check = int(year_to_check)

# or we can check with:
if year_to_check % 4 == 0:
    if year_to_check % 100 == 0:
        if year_to_check % 400 == 0:
            print(f"{year_to_check} is a leap year! It passed my nested conditionals")
        else:
            print("Not a leap year!")
    else:
        print("Leap year!")
else:
    print("Not a leap year!")


# Now let's work with multiple conditions in succession.
# If a user is attending our horse show, we need to check their age, height and if they want to get a cowboy hat with their admission.
print("Welcome to the Quarter Horse Congress! ")
show_attendee_age = input("How many years old are you? ")
show_attendee_height = input("How many inches tall are you? ")
hat_or_no_hat = input(
    "Do you want to buy a hat as well? Type 'y' if you want a hat with your admission price. Type 'n' if you do not want a hat included with your admission. ")


def qh_show_check_in(show_attendee_age, show_attendee_height, hat_or_no_hat):
    if int(show_attendee_age) >= 18:
        if int(show_attendee_height) >= 52:
            if hat_or_no_hat == 'y':
                print("Your ticket cost is $13")
            elif hat_or_no_hat == 'n':
                print("Your ticket cost is $4")
            else:
                print("Please try again and enter 'y' or 'n' for the hat option")

        else:
            ("Your ticket cost is $4")
    else:
        print("Your ticket cost is $2")


qh_show_check_in(show_attendee_age, show_attendee_height, hat_or_no_hat)

# Think about the admission costs above
# It's like we added on $9 for the hat. We could've stored their ticket cost as $4 for no hat and then added the hat fee to it like below

qh_adult_ticket = 4
qh_adult_ticket += 9  # for the hat cost
print(qh_adult_ticket)

# Let's make a pizza ordering app!
# Price the sizes:
print("Thank you for choosing to order Stormy's Pizza today")


def pizza_ordering_program():
    size = input("What size do you want? 's', 'm', or 'l'? ")
    extras = input("Do you want an all the way pizza? 'y' or 'n' ")
    pepp = input("Do you want extra pepperoni and cheese? 'y' or 'n' ")

    cost = 0

    if size == 's':
        cost += 10
    elif size == 'm':
        cost += 13
    else:
        cost += 17

    if extras == 'y':
        if size == 's':
            cost += 3
        elif size == 'm':
            cost += 4
        elif size == 'l':
            cost += 5
    else:
        cost = cost

    if pepp == 'y':
        cost += 2

    print(f"Your pizza will be ready in 20 minutes and is {cost} :) ")


pizza_ordering_program()

# Make a char counter program

name1 = "Pickle Opie Jellybean"
name2 = "Opie J"

shared_name_chars = 0

for char in name1:
    if char in name2:
        shared_name_chars += 1

if shared_name_chars <= 3:
    print(f"Those names only share {shared_name_chars}. That's not many!")
elif shared_name_chars <= 5:
    print(f"The names share {shared_name_chars} letters. That's middlin!")
else:
    print(f"Nice! {shared_name_chars} letters are in common!")


# Make a lost in the forest game. See if your user makes it home!
print("Welcome to Sequoia National Park! Find your way to the ranger station. ")
direction = input("Are you going to head east or west?")

if direction == 'west':
    print("Game over!")
elif direction == 'east':
    print("Good job heading east! Now we are at a river. ")
    swim = input("Will you swim across or wait for help? ")
    if swim == "swim":
        print("Game over! You went over the falls")
    elif swim == "wait":
        print("After 10 minutes, a ranger came, congrats!")
    else:
        print("Sorry, please type 'swim' or 'wait' ")
    print("Head back to the station, which route should she drive? ")
    path = input(
        "Should she go up the hill, through the valley, or in the dry creek bed?")
    if path == "hill":
        print("Oh no! Fallen logs, turn around")
    elif path == 'valley':
        print("Bummer! Bison in the way. Game over! :(")
    elif path == 'creek':
        print("Great choice! You made it back safely!")
    else:
        print("Please enter 'hill', 'valley', or 'creek'. :(")

else:
    print("Sorry, please enter 'east' or 'west'. ")

# we can use handy escape chars when making strings so that our quotation marks don't cause errors
print("You\'re at a great point in the course! Nice work!")
