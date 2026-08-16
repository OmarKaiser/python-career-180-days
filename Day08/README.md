Day 08 — Python Dictionaries

🎯 Learning Goal

Learn how to create, access, modify, delete, search, and loop through Python dictionaries, then combine dictionaries with functions, conditions, loops, return values, and tuple unpacking.

📚 Topics Covered

1. Creating a Dictionary

A dictionary stores data as key-value pairs.

student = {
    "name": "Omar",
    "age": 28,
    "city": "Dhaka"
}

2. Accessing Values

student["name"]
student["age"]

3. Adding a Key-Value Pair

student["course"] = "Python"

If the key does not exist, Python adds it.

4. Updating a Value

student["age"] = 29

If the key already exists, its value is updated.

5. Deleting a Key-Value Pair

del student["city"]

This removes the key-value pair.

6. Checking Whether a Key Exists

"age" in student

Returns True or False.

7. Dictionary + Functions

Dictionaries can be passed to functions:

def get_student_name(student):
    return student["name"]

8. Looping Through Keys

for key in student:
    print(key)

This iterates through the dictionary's keys.

9. Looping Through Values

for value in student.values():
    print(value)

This iterates through the dictionary's values.

10. Looping Through Keys and Values

for key, value in student.items():
    print(key, ":", value)

items() provides key-value pairs, which can be unpacked into two variables.

11. Dictionary + Conditions

Dictionary values can be used in if/else logic:

score = student["score"]

if score >= 40:
    return "Pass"
else:
    return "Fail"

12. Multiple Return Values

A function can return multiple values:

return name, score, "Pass"

They can be unpacked:

student_name, student_score, result = analyse_student(student)

This connects directly to the multiple-return-value concept learned in Day 07.

13. Final Challenge

The final challenge combines:

dictionary access

key-existence checking

functions

nested conditions

return

f-strings

The function produces a different result depending on whether a score exists and how high the score is.

🧠 Key Rules to Remember

Concept

Syntax

Purpose

Access

student["age"]

Get a value

Add

student["course"] = "Python"

Add a new key

Update

student["age"] = 29

Change an existing value

Delete

del student["city"]

Remove a key-value pair

Check

"age" in student

Check whether a key exists

Keys

for key in student

Loop through keys

Values

student.values()

Loop through values

Items

student.items()

Loop through key-value pairs

🔗 Connection to Day 07

Day 07 focused on functions, loops, conditions, return, and multiple return values.

Day 08 combines those concepts with dictionaries.

Important connection:

return name, score, "Pass"

and:

student_name, student_score, result = analyse_student(student)

This is the same multiple-value return + unpacking concept practiced in Day 07.

📁 Practice File

The complete practice code is in:

dictionaries_practice.py

Run it with:

python dictionaries_practice.py

✅ Day 08 Progress

Create a dictionary

Access values

Add key-value pairs

Update values

Delete key-value pairs

Check whether a key exists

Pass dictionaries to functions

Loop through keys

Loop through values

Loop through key-value pairs

Use dictionary values with conditions

Return multiple values

Unpack multiple returned values

Complete cumulative challenge

Complete final Day 08 challenge

🏁 Day 08 Summary

Day 08 moved from basic dictionary operations to combining dictionaries with the function concepts learned previously.

The goal was not just memorizing dictionary syntax, but learning how dictionaries work together with functions, loops, conditions, return values, and unpacking.