Day 09 — Python Data Structures: Lists, Tuples & Nested Dictionaries

Overview

Day 09 focused on lists, tuples, dictionaries, tuple unpacking, functions returning multiple values, and processing nested data structures.

Topics Covered

Lists vs. tuples

Mutable vs. immutable data

Tuple indexing

Tuple unpacking

Functions returning multiple values

Dictionaries and meaningful keys

Lists of dictionaries

Nested data access

Looping through nested data

Finding the highest value without max()

Tracking related values

Returning multiple analysis results from a function

Lists vs. Tuples

Lists are mutable:

numbers = [10, 20, 30]
numbers[1] = 50
print(numbers)

Output:

[10, 50, 30]

Tuples are immutable:

numbers = (10, 20, 30)
numbers[1] = 50

This raises:

TypeError: 'tuple' object does not support item assignment

Key difference: List → mutable; Tuple → immutable.

Tuple Unpacking

student = ("Omar", 29, "Dhaka")

name, age, city = student

print(name)
print(age)
print(city)

Output:

Omar
29
Dhaka

Tuple unpacking assigns values according to their position.

Functions Returning Multiple Values

def get_student():
    return "Omar", 29, "Dhaka"

name, age, city = get_student()

Python groups the returned values into a tuple, which can then be unpacked.

Choosing the Right Data Structure

List

Use a list when the collection may change.

shopping = ["Rice", "Eggs", "Milk"]

Tuple

Use a tuple for a fixed group of related values.

coordinate = (23.81, 90.41)

Dictionary

Use a dictionary when values have meaningful labels.

student = {
    "name": "Omar",
    "age": 29,
    "score": 85
}

For example:

student["score"]

accesses the score directly by its meaningful key.

Nested Data — List of Dictionaries

students = [
    {"name": "Omar", "score": 85},
    {"name": "Rahim", "score": 72},
    {"name": "Karim", "score": 91}
]

For example:

students[1]["name"]

returns Rahim, while:

students[1]["score"]

returns 72.

Finding the Highest Score

The maximum-value pattern starts with the first score and compares each subsequent score:

highest = students[0]["score"]

for student in students:
    score = student["score"]

    if score > highest:
        highest = score

The initial value must be set before the loop so it is not reset during every iteration.

Final Challenge

The final challenge combined a list of dictionaries, a function, a loop, dictionary access, comparison, highest-score tracking, pass-count tracking, tuple return, and tuple unpacking.

The completed solution is in data_structures_practice.py.

Expected output:

Highest student: Karim
Highest score: 91
Passed students: 5

Key Takeaways

List
  ↓
Tuple
  ↓
Tuple Unpacking
  ↓
Dictionary
  ↓
List of Dictionaries
  ↓
Nested Data Access
  ↓
Loop + Condition
  ↓
Data Analysis
  ↓
Function Returning Multiple Results

These concepts provide a foundation for working with structured data such as JSON, APIs, Pandas datasets, and machine learning data.