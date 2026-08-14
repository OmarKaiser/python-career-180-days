# ============================================
# Day 05 - Python Lists and List Processing
# ============================================


# --------------------------------------------
# Exercise 1: Remove, Insert, Pop, and "in"
# --------------------------------------------

numbers = [10, 20, 30, 40, 50]

numbers.remove(30)
numbers.insert(1, 25)
numbers.pop()

print("Exercise 1:")
print("Is 40 in the list?", 40 in numbers)
print("List:", numbers)
print()


# --------------------------------------------
# Exercise 2: List Modification
# --------------------------------------------

numbers = [5, 10, 15, 20, 25]

numbers.remove(15)
numbers.insert(1, 12)
numbers.pop()

print("Exercise 2:")
print("Is 20 in the list?", 20 in numbers)
print("List:", numbers)
print()


# --------------------------------------------
# Exercise 3: Remove the First Even Number
# --------------------------------------------

numbers = [10, 15, 20, 25, 30, 35, 40]

for number in numbers:
    if number % 2 == 0:
        numbers.remove(number)
        break

print("Exercise 3:")
print("List after removing the first even number:", numbers)
print()


# --------------------------------------------
# Exercise 4: Find the Largest Number
# --------------------------------------------

numbers = [12, 45, 7, 89, 23, 56]

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

print("Exercise 4:")
print("Largest:", largest)
print()


# --------------------------------------------
# Exercise 5: Find the Smallest Number
# --------------------------------------------

numbers = [34, 12, 56, 7, 89, 23]

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

print("Exercise 5:")
print("Smallest:", smallest)
print()


# --------------------------------------------
# Exercise 6: Largest and Smallest Even Number
# --------------------------------------------

numbers = [12, 45, 7, 89, 23, 56, 10, 34]

largest = None
smallest = None
count = 0
total = 0

for number in numbers:

    if number % 2 == 0:

        # First even number
        if largest is None:
            largest = number
            smallest = number

        else:
            if number > largest:
                largest = number

            if number < smallest:
                smallest = number

        count = count + 1
        total = total + number

print("Exercise 6:")
print("Largest Even:", largest)
print("Smallest Even:", smallest)
print("Count Even:", count)
print("Total Even:", total)
print()


# --------------------------------------------
# Exercise 7: Length, Largest, and Smallest
# --------------------------------------------

numbers = [12, 45, 7, 89, 23, 56, 10, 34]

largest = numbers[0]
smallest = numbers[0]

for number in numbers:

    if number > largest:
        largest = number

    elif number < smallest:
        smallest = number

print("Exercise 7:")
print("Total numbers:", len(numbers))
print("Largest:", largest)
print("Smallest:", smallest)
print()


# --------------------------------------------
# Exercise 8: Day 05 Final Challenge
# --------------------------------------------

numbers = [12, 45, 7, 89, 23, 56, 10, 34]

largest = numbers[0]
smallest = numbers[0]
count = 0
total = 0

for number in numbers:

    # Find largest number
    if number > largest:
        largest = number

    # Find smallest number
    if number < smallest:
        smallest = number

    # Count and sum even numbers
    if number % 2 == 0:
        count = count + 1
        total = total + number


print("Exercise 8: Final Challenge")
print("Total numbers:", len(numbers))
print("Even count:", count)
print("Even total:", total)
print("Largest:", largest)
print("Smallest:", smallest)