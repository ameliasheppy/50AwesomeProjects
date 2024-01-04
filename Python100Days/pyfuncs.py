# Let's make a list to practice recursion

words = ["Gracie", "Luna", "Pie", "Autumn"]
nums = [1, 2, 3, 4, 5]


def sum_nums(lst):
    if not lst:
        return 0

    return lst[0] + sum_nums(lst[1:])


print(sum_nums(nums))

# Factorials with recursion
# N is all nums from 1 - n


def factorial_recursive(num):
    if num == 1:
        return 1
    return num * factorial_recursive(num-1)


print(factorial_recursive(4))

# Recursive missing nums.
# If you have a list of nums, but one is missing,
# Take in a list of nums, max num and find missing num
# If none are missing, return 0
# Create a new Set and check with range if list of nums = Set


def missing_nums(nums, max_num):
    num_set = set(nums)
    for i in range(1, max_num + 1):
        if i not in num_set:
            return i
    return 0


print(missing_nums(nums, 9))
print(missing_nums(nums, 3))

# Balanced brackets


def balanced_brackets(phrase):
    closers_dict = {")": "()", "]": "[]", "}": "{}"}

    opens = set(closers_dict.values())

    openers_seen = []

    for char in phrase:
        if char in opens:
            openers_seen.append(char)

        elif char in closers_dict:
            if openers_seen == []:
                return False

            if openers_seen[-1] == closers_dict.get(char):
                openers_seen.pop()

            else:
                return False


print(balanced_brackets("{This is a dict}"))
print(balanced_brackets("[This is not a list]"))

# Merge two sorted lists:


def merge_sorted(lst1, lst2):
    merged = []
    i = 0
    j = 0
    while i < len(lst1) and j < len(lst2):
        num1 = lst1[i]
        num2 = lst2[j]

        if num1 <= num2:
            merged.append(num1)
            i += 1
        else:
            merged.append(num2)
            j += 1

    merged += lst1[i:] + lst2[j:]
    return merged


print(merge_sorted([1, 6, 8], [0, 2, 9]))
