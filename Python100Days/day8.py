from day8art import logo

# Why do we use functions?
# They're reusable little chunks of code.


def hey_there_friends(arr):
    for name in arr:
        print(f"Hey there {name}")


names = ["Jesse", "Jay", "Jacob"]

hey_there_friends(names)


def say_hello_unique(name):
    print(f"Hello {name}")


today_i_am_talking_to = input("Greetings! What is your name? ")
say_hello_unique(today_i_am_talking_to)

# Our functions can take in multiple inputs like this:


def vacation_city(date, location="NagsHead, NC"):
    print(f"Have fun in {location}, {date}, Smith Family!")


vacation_city("04-30-2024-09-07-24")

# Positional args mean that Python will look at the positions of where our args are to use them
# Keyword arguments mean that we can do this:


def algebra(a, b, c):
    return (a + b) - c


print(algebra(c=3, b=2, a=7))

# Fence Paint Area Calculator:


def paint_will_cover(height, width, covers):
    number_of_cans = (height * width) / covers
    return number_of_cans


fence_height = int(input("What is the height of your fence? "))
fence_width = int(input("What is the width of your fence? "))
fence_coverage = 5
print(paint_will_cover(height=fence_height,
      width=fence_width, covers=fence_coverage))

# We can check to see if a number is prime or not


def is_your_number_even(num):
    if num % 2 == 0:
        print(f"{num} is even")
    else:
        print(f"{num} is odd")


is_your_number_even(27)
is_your_number_even(2)

'''
Loop to Check for Divisors:
for i in range(2, int(num ** 0.5) + 1):
This loop iterates from 2 to the square root of the number (num ** 0.5).
The loop's purpose is to check for divisors of num. If num has any divisors apart from 1 and itself, it's not a prime number.
Checking for Divisibility:

if num % i == 0:
Inside the loop, it checks if num is divisible by the current value of i (the loop variable).
If num is divisible by i without any remainder, it means num is not a prime number since it has a divisor other than 1 and itself.
In this case, it returns False immediately.
'''


def is_prime(number):
    if number < 2:
        print(f"{number} is not prime")
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            print(f"{number} is not prime")
            return False
    print(f"{number} is prime")
    return True


is_prime(3)
is_prime(30)

# A fun little encryption activity that we can do is to make a caesar cipher where we do a shift of the alphabet over by an int.

print(logo)


def caesar(direction, text, shift):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    shifted_text = ""
    if direction == "decode":
        shift *= -1

    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = (position + shift) % len(alphabet)
            shifted_text += alphabet[new_position]
        else:
            shifted_text += letter  # Preserve non-alphabetic characters

    print(f"The {direction}d text is now: {shifted_text}")


continue_the_cipher = True
while continue_the_cipher:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    text = input("Type your message: \n").lower()
    shift = int(input("Type the shift number: \n"))

    # O(n)  <---- bc n is the length of the input text, but may be higher due to the shift.

    caesar(direction, text, shift)
    result = input("Type 'yes' if you want to go again. If not, type 'no'. \n")
    if result == "no":
        continue_the_cipher = False
        print("Goodbye!! :)")


'''
User Input:

If the user types "encode", the direction remains as is, indicating that the text should be encoded (shifted forward in the alphabet).
If the user types "decode", it indicates that the text should be decoded (shifted backward in the alphabet).
Changing Direction for Decoding:

When the direction is "decode", it means we need to reverse the shifting direction to decode the message correctly.
The shift *= -1 line is a shorthand way of saying "take the value of shift and multiply it by -1".
If shift is positive, multiplying it by -1 turns it negative.
If shift is negative, multiplying it by -1 turns it positive.
This operation effectively flips the direction of the shifting, enabling decoding. For example:
If the original shift is +3 (encoding), shift *= -1 changes it to -3 (decoding).
If the original shift is -2 (encoding), shift *= -1 changes it to +2 (decoding).
So, shift *= -1 dynamically alters the shift value based on the user's choice of encoding or decoding. If it was set to encode (positive shift), it turns it into a negative shift for decoding, and if it was set to decode (negative shift), it turns it into a positive shift for encoding.
'''
