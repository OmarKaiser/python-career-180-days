# Day 13: Lambda Functions and Sorting

# 1. Basic lambda function
square = lambda x: x * x
print("Square:", square(5))


# 2. Lambda with multiple parameters
add = lambda a, b: a + b
print("Addition:", add(10, 20))


# 3. Lambda returning a Boolean value
is_even = lambda number: number % 2 == 0
print("Is 12 even?", is_even(12))


# 4. Lambda with abs()
absolute_difference = lambda a, b: abs(a - b)
print("Absolute difference:", absolute_difference(4, 10))


# 5. Sorting dictionaries by age
students = [
    {"name": "Omar", "age": 30},
    {"name": "Rahim", "age": 25},
    {"name": "Karim", "age": 28}
]

sorted_by_age = sorted(
    students,
    key=lambda x: x["age"]
)

print("Sorted by age:", sorted_by_age)


# 6. Sorting by score from highest to lowest
students = [
    {"name": "Omar", "score": 85},
    {"name": "Rahim", "score": 92},
    {"name": "Karim", "score": 78}
]

sorted_by_score = sorted(
    students,
    key=lambda x: x["score"],
    reverse=True
)

print("Sorted by score:", sorted_by_score)


# 7. Independent practice: sorting employees by salary
employees = [
    {"name": "Omar", "salary": 50000},
    {"name": "Rahim", "salary": 65000},
    {"name": "Karim", "salary": 45000}
]

sorted_employees = sorted(
    employees,
    key=lambda x: x["salary"]
)

print("Sorted employees:", sorted_employees)