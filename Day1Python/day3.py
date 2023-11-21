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
