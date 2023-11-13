# Python's 2 main number types are int and float

from functools import reduce
from collections import OrderedDict
from collections import namedtuple
from collections import Counter
print(type(1))
print(type(9.3))
print(type(4E2))

print(10+3)
print(10-3)
print(10*3)
print(10 ** 3)
print(f'The / operator in Python will give you a remainder')
print(10/3)
print(f'The // in Python uses floor division and does not give you decimals. It returns a float')
print(10//3)
print(f'The % in Python is the modulo operator. It Returns the remainder. It is very useful for deciding if a number is even or odd')
print(10 % 3)

# Basic fun functions:
print(pow(5, 2))
print(abs(-50), f'Should be 50, bc the abs of -50 is 50')
print(round(8.9383748, 2), f'This should round my huge number to 2 decimal places')

print(bin(512), f'Using bin should convert an entered number into the correct binary format')

print(hex(623), f'Using hex(623) should convert the number entered into hexadecimal format.')

# We can also do type conversion with Python. Let's convert some strings into numbers:
# age = input("How old are you?")
# print(type(age), age, f'Before type conversion')
# age = int(age)
# print(type(age), age, f'Before type conversion')

# pi = input('What is the value of pi?')
# pi = float(pi)
# print(type(pi))

# strings in Python are stored as sequences of letters in memory
# they are immutable, but you can reassign them

print(type("Hi"))
# We can use escape characters to make sure that our apostrophes and quotation marks do not interfere with our strings
print('I\'m thirsty')
print("I'm thirsty!")
print('I am putting this on \n a \n new  \n line!')
print("I am adding in a \t tab")

print('Hey you!!'[4])
name = "Izzy Stanley"
print(name)
print(name[::-1], f'Did this reverse?')
print(name[-1])
print(name[0:])
print(name[1:4])
print(name[::1])
print(name[0:12:2])

# using the : symbol with a string is called slicing and it follows the format [start: end : step]

'Hi there ' + 'Stormy was made with concatenation!'


def contamination(str, char):
    return char * len(str)


print(contamination("Stars", "*"))

# Basic functions with Python:
print(len("Pup"))  # 3

# Basic Methods with Python:
print(('   I am alone........            ').strip())
print(("On an island").strip("d"))
print(("Life is Good!").split())
print(("Horses are just big dogs!").replace("Horses", "All horses"))
print(("Need to make fire").startswith("Need"))
print(("and cooking rice.").endswith("rice."))
print(("still there?").upper())
print(("HELLO>!>!").lower())
print(("Ok, I am done!").capitalize())
print(("Oh hi there!").find("h"))
print(("Oh, hello there my friends!").count("e"))


# string formatting with Python:
name1 = 'Andrei'
name2 = 'Sunny'
print(f'Hello there {name1} and {name2}')
print('Hello there {} and {} '.format(name1, name2))
print('Hello there %s and %s ' % (name1, name2))

# lets make a quick palindrome check with Python
word = 'reviver'
p = bool(word.find(word[::1]) + 1)
print(p)

# or we can
word3 = "cats"
print(word3 == word3[::-1])

# Booleans are True or False. They are used in a lot of comparison and logical operations in Python
# all of the below evaluate to False. Everything else will evaluate to True in Python.
print(bool(None))
print(bool(False))
print(bool(0))
print(bool(0.0))
print(bool([]))
print(bool(['cat']))
print(bool({}))
print(bool({'dog': 'the best'}))
print(bool(()))
print(bool(''))
print(bool('is this true now?'))
print(bool(range(0)))
print(bool(set()))
print(bool(1))

# Lists are mutable in Python
# assume that the list won't mutate for each example below
my_list = [1, 2, 2, '3', True]
print(len(my_list))
print(my_list.index('3'))
print(my_list.count(2))

print(my_list[3])
print(my_list[1:])
print(my_list[:1])
print(my_list[-1])
print(my_list[::1])
print(my_list[::-1])
print(my_list[0:3:2])

# now let's append some stuff to the list!
print(my_list * 2)
print(my_list + [100])
print(my_list.append(100))
print(my_list.extend([100, 200]))
print(my_list.insert(2, "!!!!!"))
print(' '.join(["Hello", "there", "!"]))

# we can easily copy a list:
basket = ["apples", "pears", "oranges"]
new_basket = basket.copy()
print(new_basket)
new_basket_2 = basket[:]
print(new_basket_2 * 2)

# Remove from our list:
print([1, 2, 3, 4, 5, 6].pop(1))
print([1, 2, 3, 4].pop(1))
print([1, 2, 3, 4].remove(2))
print([1, 2, 3].clear())
del [1, 2, 3][0]

# We can do ordering:
my_out_of_order_list = [1, 2, 5, 1, 4, 0.5]
print(my_out_of_order_list.sort(), '.sort()')
print(my_out_of_order_list.sort(reverse=True), 'sort')
print(my_out_of_order_list.reverse(), 'sort')
print(sorted(my_out_of_order_list))
print(list(reversed(my_out_of_order_list)))

# handy operations for my list!
print(1 in my_out_of_order_list)
print(min(my_out_of_order_list))
print(max(my_out_of_order_list))
print(sum(my_out_of_order_list))

# how to get the first and last element from a list?
first, *x, last = my_out_of_order_list

print(first, 'first')
print(last, 'last')
print(*x, '*x')


# working with matrices
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(matrix)
print(matrix[2][0], 'should be the first first of the third row in the matrix')

# let's loop through a matrix by its rows:
for row in range(len(matrix)):
    for col in range(len(matrix)):
        print(matrix[row][col])

# we can transform a matrix into a list:
print([matrix[row][col] for row in range(len(matrix))
       for col in range(len(matrix[0]))])

# we can combine our columns with zip and *:
print([x for x in zip(*matrix)])

# list comprehensions are weird, but fun!
a = [i for i in 'hello']
print(a)
b = [i*2 for i in [1, 2, 3, 4]]
print(b)
c = [i for i in range(0, 7) if i % 2 == 0]
print(c)


# here are some more difficult functions:
list_of_chars = list("Helllloooo")
print(list_of_chars)
sum_of_elements = sum([4, 4, 4, 4, 4])
print(sum_of_elements)
element_sum = [sum(pair) for pair in zip([1, 2, 3], [4, 5, 6])]
print(element_sum)
sorted_by_second = sorted(['Hi', 'you', 'man'], key=lambda el: el[1])
print(sorted_by_second)
sorted_by_key = sorted([
    {'name': 'Bina', 'age': 30},
    {'name': 'Andy', 'age': 33},
    {'name': 'Jackson', 'age': 4}],
    key=lambda el: (el['age'])
)

print(sorted_by_key)

# commenting out the below bc I keep writing to my file!
# read a line of a file into a list:
# with open("myfile.txt") as f:
#     lines = [line.strip() for line in f]
#     print(lines)

# with open("myfile.txt") as file:
#     content = file.read()
#     print(content)

# the below will over write all of my file contents
# with open("myfile.txt", 'w') as file:
#     file.write("I am sending some new text to my text file!")

# with open("myfile.txt", 'a') as file:
#     file.write("\nAppending some text to the file")


# with open("myfile.txt", 'a') as file:
#     file.write("\nAppending even more!")

# with open("myfile.txt") as file:
#     content = file.read()
#     print(content)

# Dictionaries in Python are also known as mappings or hash atbles. They are k/v pairs that are guaranteed to retain order of insertion starting with Python 3.7

my_dict = {'nombre': "Peanut On A Railroad Track",
           "age": 8, "disney_princess": False}

print(my_dict['nombre'])
print(len(my_dict))
print(list(my_dict.keys()))
print(list(my_dict.values()))
print(list(my_dict.items()))
my_dict['favorite_snack'] = "Popcorn"
print(my_dict.get('age'))  # returns none if the key does not exist
# returns default (2nd param) if the key is not found
print(my_dict.get('ages', 0))
my_dict.update({'cool': True})
# below uses dictionary unpacking
# ** allows you to use the k/v pairs of one dict to create or update another dict
print({**my_dict, **{'cool': True}})
# We can also add multiple kv pairs with dict unpacking
print({**my_dict, **{'hiker': True, 'hobby': 'soccer'}})

# we can also construct dictionaries:
new_dict = dict([['name', 'Andrew'], ['age', 23], ['dogs', True]])
print(new_dict)
# or we can zip dicts together:
# Creates a dict from two collections.
new_dict_zip = dict(zip(['name', 'age', 'magic_power', 'favourite_snack'], [
                    'Andrei', 32, False, 'tostadas']))
print(new_dict_zip, 'all the dict created with zip')
new_dict_zip.pop('favourite_snack')
print(new_dict_zip, 'popped off snack')


# dictionary comprehension
# dictionary comprehension
result_dict = {key: value for key, value in new_dict_zip.items()
               if key == "name" or key == "age"}
print(result_dict)

# Tuples are like lists but they are used for immutable things that don't change
tuple_number_one = ('apples', 'grapes', 'mango', 'grapes')
apple, grapes, mango, grapes = tuple_number_one  # this is tuple unpacking
print(tuple_number_one)
print(len(tuple_number_one))
print(tuple_number_one[2])
print(tuple_number_one[-1])

# Immutability
# my_tuple[1] = 'donuts'  # TypeError
# my_tuple.append('candy')# AttributeError

# tuple methods:
print(tuple_number_one.index('grapes'))
print(tuple_number_one.count('grapes'))

# zip:
print(list(zip([1, 2, 3], [4, 5, 6])))

# we can also unzip
z = [(1, 2), (3, 4), (5, 6), (7, 8)]
print(z)
def unzip(z): return list(zip(*z))


print(unzip(z))

# sets are an unordered collection of unique elements
my_set = set()
my_set.add(1)
my_set.add(100)
my_set.add(100)  # check it out, no duplicates will be added!
print(my_set)

new_list_for_a_set = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 4, 1]
set(new_list_for_a_set)

# my_set.remove(1000)  # raises a keyError if doesn't exist
my_set.discard(100)  # Doesn't raise an error if not found
my_set.clear()
print(my_set, ' is this an empty set?')
new_set = {1, 2, 3}.copy()
print(new_set)

# we can do unions with sets
set1 = {1, 2, 3}
set2 = {3, 4, 5}
set3 = set1.union(set2)
set4 = set1.intersection(set2)
set5 = set1.difference(set2)
set6 = set1.symmetric_difference(set2)
print(set3)
print(set4)
print(set5)
print(set6)
print(set1.issubset(set2))
print(set1.issuperset(set2))
# False --> return True if two sets have a null intersection
print(set1.isdisjoint(set2))

# Create a frozenset
my_frozenset = frozenset([1, 2, 3, 4])
print(my_frozenset)

# Attempt to modify the frozenset (this will result in an error)
# my_frozenset.add(5)  # This will raise an AttributeError

# None is used for absence of a value and can be used to show that nothing has been assigned to an obj
print(type(None))
a = None
print(a)

# comparision operators:
# ==                   # equal values
#!=                   # not equal
# >                    # left operand is greater than right operand
# <                    # left operand is less than right operand
# >=                   # left operand is greater than or equal to right operand
# <=                   # left operand is less than or equal to right operand
# <element> is <element> # check if two operands refer to same object in memory
print(False is bool)

# logical operators:
print(1 < 2 and 4 > 1)  # True
print(1 > 3 or 4 > 1)  # True
print(1 is not 4)     # True
print(not True)       # False
print(1 not in [2, 3, 4])  # True

# loops with Python
iterator_list = [1, 2, 3, 4]
iterator_tuple = (1, 2, 3, 4)
iterator_list_two = [(1, 2), (3, 4), (5, 6)]
iterator_dict = {'a': 1, 'b': 2, 'c': 3}

for num in iterator_list:
    print(num)

for num in iterator_tuple:
    print(num)

for num in iterator_list_two:
    print(num)

for num in '12345':
    print(num)

for k, v in iterator_dict.items():
    print(k)
    print(v)


count = 0

while count < 5:
    print(f"Current count: {count}")

    if count == 2:
        print("Breaking out of the loop")
        break  # This will exit the loop when count is 2
    if count == 1:
        print("Skipping this iteration.")
        count += 1
        continue  # This will skip the rest of the loop body and move to the next iteration
    print("Still inside the loop")
    count += 1

# we can set an action up to continue until the user quits.
# msg = ''
# while msg != 'q':
    # msg = input("What should I do? ")
    # print(msg)

# Range is not inclusive of the high number that you give to it.
print(range(5))
print(range(1, 3))
print(list(range(0, 9, 2)))

# range is versatile and commonly used in scenarios where you need to perform an action a specific number of times or generate sequences of numbers.


# enumerate in Python iterates over a seq such as a list, tuple or string while keeping track of the index of the current item. It returns pairs of index and value for each item in the sequence.
# the default start value is 0, but you can enter a start number if you want
fruits_to_enum = ['apple', 'banana', 'cherry', 'dragonfruit']
# again, we don't need the start value, I am just trying it out
for index, fruit_to_enum in enumerate(fruits_to_enum, start=2):
    print(f"Index: {index}, Fruit: {fruit_to_enum}")

# enumerate is handy when you need both the index and the value of elements while iterating over a seq. It's commonly used in loops when you want to keep track of the position of items.


def find_index(lst, target):
    for index, value in enumerate(lst):
        if value == target:
            return index

    return -1


target_fruit = 'banana'
index = find_index(fruits_to_enum, target_fruit)
if index != -1:
    print(f"The aisle of '{target_fruit}' is {index}")
else:
    print(f"'{target_fruit}' is not found in this store!")

for i, el in enumerate("Stormy"):
    print(f"{i}, {el}")

colors = ['red', 'blue', 'yellow', 'blue', 'red', 'blue']
counter = Counter(colors)  # Counter({'blue': 3, 'red': 2, 'yellow': 1})
print(counter.most_common()[0])  # ('blue', 3)
print(counter.values())
print(counter.items())
print(counter.keys())


# A tuple is an immutable and hashable list.
# A named tuple is its subclass with named elements. It's a lightweight ds in Python that allows you to define simple classes for storing data without the overhead of a full class definition.
# Lets create a 'Point' named tuple with 'x' and 'y' fields and an instance 'p' of this tuple to demonstrate accessing elements by both index and name, using 'gettattr' and accessing the field names with '_fields'

Point = namedtuple("Point", "x y")
p = Point(1, 2)
print(p)
print(p[0], 'p[0]')
print(p.x, 'p.x')
print(getattr(p, 'y'), 'getattr')
print(p._fields, 'p._fields')
print(p._asdict(), 'as_dict')
new_point = p._replace(x=10)
print(new_point)
print(p._asdict(), 'as_dict after a replace')

Person = namedtuple("Person", "height")
jesse = Person(height=290)
print(f'{jesse.height}')

# orderedDict maintains the order of insertion
programmers = OrderedDict()
programmers["Tim"] = ["Python", "JS"]
programmers["Sarah"] = ["C++"]
programmers["Bia"] = ["Ruby", "Python", "Go"]

for name, langs in programmers.items():
    print(name + '-->')
    for lang in langs:
        print('\t' + lang)

# Functions with Python.
#   *args and **kwargs
# *is a splat and it expands a collection in positional args.
# ** is a splatty splat and it expands a dict into kwargs
args = (1, 2)
kwargs = {'x': 3, 'y': 4, 'z': 5}


def some_func(*args, **kwargs):
    print(f"Positional Arguments: {args}")
    print(f"Keyword Arguments: {kwargs}")


some_func(*args, **kwargs)

# inside function definitions:
# Splat combines zero or more positional args into a tuple, while splatty splat combines zero or more keyword args into a dict


def add(*a):
    return sum(a)


print(add(4, 4, 5, 5))

# Python uses lambda functions too:
n = 3
factorial = reduce(lambda x, y: x*y, range(1, n+1))
print(factorial)

# range(1, n+1): This creates a sequence of numbers from 1 to n+1. In your example, if n is 3, then range(1, 4) creates the sequence [1, 2, 3].

# lambda x, y: x*y: This is a lambda function, a small anonymous function. It takes two arguments (x and y) and returns their product (x*y). In simpler terms, it's like a little math formula: "multiply x and y together."

# reduce function: This is a function from the functools module in Python. It's used to successively apply the lambda function to the elements of the sequence, reducing them to a single value.

# factorial =: This assigns the result of the reduce operation to the variable factorial.

# Now, let's see how it works with an example:

# Iteration 1: 1 * 2 (initial x is 1, and y is 2) => Result: 2
# Iteration 2: 2 * 3 (now, x is the result from the previous step, which is 2, and y is 3) => Result: 6
# So, the final result assigned to factorial is 6, which is the factorial of 3.

# In simpler terms, the code is saying: "Hey, reduce this list of numbers (1, 2, 3) by multiplying them together," and the answer is 6!


# lets do a fibonacci with a lambda now:
def fib(n): return n if n <= 1 else fib(n-1) + fib(n-2)


result = fib(10)
print(result)

# comprehensions in Python are concise ways to create lists, sets, iterators, or dicts. They provide a compact and readable syntax for generating sequences or performing transformations on existing ones.
# conciseness and readability
my_list_comprehension = [i + 1 for i in range(10)]
print(my_list_comprehension)

# Here is a set comprehension with a conditional in it
my_set_comprehension = {i for i in range(10) if i > 5}
print(my_set_comprehension)

# A generator expression is similar to list comprehensions that use parentheses
my_iterator_comprehension = (i + 7 for i in range(10))
# since we made a generator, now we need to iterate over it to get its values:
for value in my_iterator_comprehension:
    print(value)

# lets use a comprehenstion to make a dict in a concise manner:
my_generator_dict = {i: i*2 for i in range(11)}
print(my_generator_dict)


# comprehensions can help with performance bc they can be more efficient that for loops in terms of speed and mem usage. They are optimized internally in CPython.
output = []
for i in range(3):
    for j in range(4):
        output.append(i + j)
print(output, 'from a nested for loop')

output_with_comprehension = [i+j for i in range(3) for j in range(3)]
print(output_with_comprehension,
      'from the comprehension equivalent of a nested for loop')

# ternary expressions in python are concise ways to write conditional statements.
# we can replace negative numbers with 0:
ternary_numbers = [2, -1, 0, 3, -4, 6, 0, -12]

result_ternary_numbers = [num if num >= 0 else 0 for num in ternary_numbers]
print(result_ternary_numbers)


# let's categorize numbers as positive or negative:
categories = ['positive' if num > 0 else 'negative' if num <
              0 else 'zero' for num in ternary_numbers]
print(categories)

# capitalize words longer than 3 letters:
ternary_words = ["cat", "apple", "boxer", "dog", "stryker", "stormy"]
capitalized = [word.capitalize() if len(
    word) > 3 else word for word in ternary_words]
print(capitalized)

# convert temp to celsius if fahrenheit is given:
temperature_ternaries = [('F', 32), ("C", 20), ("F", 100), ("C", 10)]
converted_temps = [temp if unit == "C" else (
    5/9)*(temp-32) for unit, temp in temperature_ternaries]
print(converted_temps)

# lets learn about map filter and reduce.
# map through numbers and double them
map_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
squared_map_numbers = list(map(lambda x: x**2, map_numbers))
print(squared_map_numbers)

# filter even numbers from a list
even_numbers = list(filter(lambda x: x % 2 == 0, map_numbers))
print(even_numbers)

# calculate the product of a list of nums
product = reduce(lambda acc, x: acc * x, map_numbers)

product_pythonic = 1
for num in map_numbers:
    product_pythonic *= num

print(product_pythonic)

# lets use filter to filter the even numbers from a list
even_numbers_with_filter = list(filter(lambda x: x % 2 == 0, map_numbers))

even_numbers_filtered_with_python = [x for x in map_numbers if x % 2 == 0]

print(even_numbers_with_filter, 'Filtered with a lambda')
print(even_numbers_filtered_with_python,
      'filtered with a python list comprehension')

conditions = [False, True, False]
result_any = any(conditions)
print(result_any)

conditions_all = [True, 1, 3, True]
conditions_all_false = [True, 1, 3, False]
result_all = all(conditions_all)
result_all_false = all(conditions_all_false)
print(result_all)
print(result_all_false)


# closures in Python:
# a closure is a nested function references a value of its enclosing function and then the enclosing function returns the nested function
def get_multiplier(a):
    def out(b):
        return a * b
    return out


multiply_by_three = get_multiplier(3)
print(multiply_by_three(10))

# if multiple nsted functions within an enclosing function reference the same value, that value gets shared.
# to dynamically access the functions first free var us
print(multiply_by_three.__closure__[0].cell_contents, 'cell contents')

# we are making a function called memoize that takes another function ('func') as its argument. This is an example of a decorator function. Decorators in python are a powerful way to modify or extend the behvaior of functions.


def memoize(func):
    cache = {}

# This line initializes an empty dictionary named cache. This dictionary will be used to store the results of previous function calls to avoid redundant computations.
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]

    return wrapper


# Usage
@memoize
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# scope with Python
# if a var is assigned to anywhere in the scope, it is regarded as a local var, unless it is declare as 'global' or 'nonlocal'


def get_counter():
    i = 0

    def out():
        nonlocal i
        i += 1
        return i
    return out


counter = get_counter()
print(counter(), counter(), counter())

global_variable = 5


def modify_global():
    global global_variable
    global_variable += 1
    print("Inside Function:", global_variable)


modify_global()
print("Outside Function:", global_variable)
