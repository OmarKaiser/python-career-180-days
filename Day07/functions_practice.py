# Day 07 — Python Functions: Practical Practice


# 1. Function Chaining

def square(number):
    return number * number


def add_ten(number):
    return number + 10


def double(number):
    return number * 2


result = square(5)
result = add_ten(result)
result = double(result)

print("Pipeline result:", result)


# 2. Function + List + Loop

numbers = [2, 4, 6, 8]


def process_numbers(numbers):
    total = 0

    for number in numbers:
        square = number * number
        total = total + square

    return total


result = process_numbers(numbers)
print("Sum of squares:", result)


# 3. Function + Condition + List

numbers = [2, 5, 8, 11, 14, 17, 20]


def calculate_even_square_total(numbers):
    total = 0

    for number in numbers:
        if number % 2 == 0:
            square = number * number
            total = total + square

    return total


result = calculate_even_square_total(numbers)
print("Even square total:", result)


# 4. Function Returning Two Results

numbers = [2, 5, 8, 11, 14, 17, 20]


def analyze_even_numbers(numbers):
    count = 0
    total = 0

    for number in numbers:
        if number % 2 == 0:
            count = count + 1
            total = total + number

    return count, total


even_count, even_total = analyze_even_numbers(numbers)

print("Even count:", even_count)
print("Even total:", even_total)


# 5. Find the Largest Number Without max()

numbers = [34, 12, 56, 7, 89, 23]


def find_largest(numbers):
    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

    return largest


result = find_largest(numbers)
print("Largest:", result)


# 6. Find the Smallest Number Without min()

def find_smallest(numbers):
    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest


result = find_smallest(numbers)
print("Smallest:", result)


# 7. One Function — Multiple Results

numbers = [34, 12, 56, 7, 89, 23]


def analyze_numbers(numbers):
    largest = numbers[0]
    smallest = numbers[0]
    total = 0

    for number in numbers:
        total = total + number

        if number > largest:
            largest = number

        if number < smallest:
            smallest = number

    return largest, smallest, total


largest, smallest, total = analyze_numbers(numbers)

print("Largest:", largest)
print("Smallest:", smallest)
print("Total:", total)


# 8. Final Challenge — Combined Analysis

numbers = [15, 8, 23, 42, 7, 16, 31, 10]


def analyze_number_details(numbers):
    count = 0
    total = 0
    largest = numbers[0]
    smallest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number

        if number < smallest:
            smallest = number

        if number % 2 == 0:
            count = count + 1
            total = total + number

    return count, total, largest, smallest


even_count, even_total, largest, smallest = analyze_number_details(numbers)

print("Even count:", even_count)
print("Even total:", even_total)
print("Largest:", largest)
print("Smallest:", smallest)