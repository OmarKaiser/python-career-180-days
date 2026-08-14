# Day 06 — Python Functions


# Exercise 1 — Your First Function

def greet():
    print("Hi, Omar")


greet()


# Exercise 2 — Function with a Parameter

def greet_name(name):
    print("Hi,", name)


greet_name("Omar")
greet_name("Python")


# Exercise 3 — Two Parameters

def add(a, b):
    print("Sum of a and b:", a + b)


add(10, 20)


# Exercise 4 — Return

def add_numbers(a, b):
    return a + b


result = add_numbers(10, 20)
print(result)


def multiply(a, b):
    return a * b


result = multiply(5, 6)
print(result)


# Exercise 5 — Square

def square(number):
    return number * number


result = square(5)
print(result)


# Exercise 6 — Function + If

def check_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"


result = check_even(35)
print("Number is:", result)


# Exercise 7 — Function + Calculation

def double(number):
    return number * 2


result = double(5)
print(result)


# Exercise 8 — Function with Multiple Conditions

def grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    else:
        return "F"


result = grade(69)
print(result)


# Exercise 9 — Function + List + Loop

numbers = [10, 15, 20, 25, 30, 35, 40]


def count_even(numbers):
    count = 0

    for number in numbers:
        if number % 2 == 0:
            count = count + 1

    return count


result = count_even(numbers)
print(result)


# Exercise 10 — Function to Calculate the Total

numbers = [10, 20, 30, 40, 50]


def calculate_total(numbers):
    total = 0

    for number in numbers:
        total = total + number

    return total


result = calculate_total(numbers)
print(result)


# Exercise 11 — Even Total Function

numbers = [10, 15, 20, 25, 30, 35, 40]


def calculate_even_total(numbers):
    total = 0

    for number in numbers:
        if number % 2 == 0:
            total = total + number

    return total


result = calculate_even_total(numbers)
print(result)


# Exercise 12 — Function with Two Results

numbers = [10, 15, 20, 25, 30, 35, 40]


def calculate_even(numbers):
    count = 0
    total = 0

    for number in numbers:
        if number % 2 == 0:
            count = count + 1
            total = total + number

    return count, total


count, total = calculate_even(numbers)

print("Even Count:", count)
print("Even Total:", total)


# Mini Challenge — Analyze Numbers

numbers = [12, 45, 7, 89, 23, 56, 10, 34]


def analyze_numbers(numbers):
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


count, total, largest, smallest = analyze_numbers(numbers)

print("Even Count:", count)
print("Even Total:", total)
print("Largest:", largest)
print("Smallest:", smallest)