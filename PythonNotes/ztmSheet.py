# Python's 2 main number types are int and float

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
