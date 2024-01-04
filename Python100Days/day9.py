# Dictionaries in Python store k/v pairs. Think of them like a real life dictionary. Or a lookup table.
fun_with_dictionaries = {"Key": "Value"}
print(fun_with_dictionaries.keys())
print(fun_with_dictionaries.values())
print(fun_with_dictionaries.items())
# We can also just access with a key!
print(fun_with_dictionaries["Key"])
# A really common error is when we are accessing something that doesn't exist and we get a KeyError.
# We would also get an error if we access the wrong data type
# print(fun_with_dictionaries[Key])
# See! That's not a string, so it's not the key


# To retrieve items from a dict, add on square brackets to the dict_name and then the key in them.
# What if we want to add a key, but programmatically?

# Adding new items to dict:
fun_with_dictionaries["New key"] = "Adding another key and value!"
print(fun_with_dictionaries)


# Want to wipe out a dict?
# fun_with_dictionaries = {}
# print(fun_with_dictionaries)
# That is helpful to clear a user's progress or when a game restarts.

# Can edit an item in a dict:
fun_with_dictionaries["New key"] = "Edited the new key!"
print(fun_with_dictionaries)


# How to loop through a dict.
for item in fun_with_dictionaries:
    print(item, "Those are the keys!")
#           REMEMBER< when you loop through a dict, it does not actually loop through each of the k/v pairs, it loops through each of the keys!!!!

# Want both?
for item in fun_with_dictionaries:
    print(item)
    print(fun_with_dictionaries[item], "getting both with retrieval brackets!")

grades = {
    "Bill": 89,
    "Maddy": 100,
    "Jessica": 103,
    "Samantha": 74
}

written_message = {}

for student in grades:
    score = grades[student]

    if score > 90:
        written_message[student] = "Outstanding"
    elif score > 80:
        written_message[student] = "Exceeds expectations"
    elif score > 70:
        written_message[student] = "Passing!"
    else:
        written_message[student] = "Fail, we will work and improve this!"

print(written_message)

# We can also nest! It is more complex, but really handy to store things.

dogs = {
    "GSD": "Jake",
    "Boxer": "Pilot"
}

dogs["Border Collie"] = "Em"
dogs["JRT"] = "Boomer"
print(dogs)

travels = {
    "North Carolina": ["Nags Head", "Rodanthe", "Raleigh", "Rocky Mount"],
    "Georgia": {"cities_visited": ["Buford", "Flowery Branch", "Atlanta", "Tiger"], "total_visits": 7}
}

# Lists are ordered and can be accessed by indexes.
# So we can put our nested dicts and lists in a big list:
nest_of_fun = [{"Hikes": ["Mt Sterling", "Stone Mountain"], "ATL": {
    "aquarium": "dolphin show", "stone mountain park": "hike and park time"}}]

nest_of_fun.append({"Buford": ["Publix", "Buccees"]})

print(nest_of_fun[0]["Hikes"], "<------ Access the dict in a list")
print(nest_of_fun[0])
print(nest_of_fun, "**************************************")

summer_2024 = [
    {
        "state": "NC",
        "cities": ["Nags Head", "Kitty Hawk"],
        "days": 11
    },
    {
        "state": "GA",
        "cities": ["Atlanta", "Flowery Branch"],
        "days": 9
    },
    {
        "state": "NY",
        "cities": ["Warwick", "Walkill", "Fishkill"],
        "days": 4
    },
]

print(summer_2024[0]["state"])
print(summer_2024[1]["cities"])
print(summer_2024[2]["cities"][2])


def add_new_trip(name, cities_to_visit, length_in_days):
    new_trip = {}
    new_trip["state"] = name
    new_trip["cities"] = cities_to_visit
    new_trip["days"] = length_in_days

    summer_2024.append(new_trip)


add_new_trip("Colorado", ["Colorado Springs", "ElkTown"], 10)
print(summer_2024)

# Let's make a fancy auction program:
print("Welcome to the Boxer Foundation toy auction!")


def find_highest_bidder(bids_submitted):
    highest = 0
    winner = ""
    for bidder in bids_submitted:
        bid_amount = bids_submitted[bidder]
        if bid_amount > highest:
            highest = bid_amount
            winner = bidder
    print(f"The winner is {winner.title()} with a high bid of ${highest}")


# Our key will be the bidder name
# Value will be the $ amount that they bid
bids = {}
more_bids = False
while not more_bids:
    bidder = input("What is your name? ")
    bidder_bid = int(input("What is your bid? "))
    bids[bidder] = bidder_bid

    print(bids)
    print(bids[bidder])
    more_bids = input("Are there other bids on this item? Type 'y' or 'n' ")
    if more_bids == "n":
        more_bids = True
        find_highest_bidder(bids)
    elif more_bids == "y":
        more_bids = False
