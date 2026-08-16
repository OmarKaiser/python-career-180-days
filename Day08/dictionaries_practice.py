# Day 08 — Python Dictionaries

student = {
    "name": "Omar",
    "age": 28,
    "city": "Dhaka"
}

# Add, update, and delete dictionary data
student["course"] = "Python"
student["age"] = 29
student["score"] = 85
del student["city"]

# Access values
print(student["name"])
print(student["age"])
print(student["course"])

# Print dictionary
print(student)

# Check whether keys exist
print("age" in student)
print("city" in student)


# Dictionary + Function
def get_student_name(student):
    return student["name"]


result = get_student_name(student)
print(result)


# Dictionary + Function + Condition
def check_key(student, key):
    if key in student:
        return "Found"
    else:
        return "Not found"


print(check_key(student, "age"))
print(check_key(student, "course"))
print(check_key(student, "city"))


# Loop through dictionary keys
def print_keys(student):
    for key in student:
        print(key)


print_keys(student)


# Loop through dictionary values
def print_values(student):
    for value in student.values():
        print(value)


print_values(student)


# Loop through dictionary items
def print_items(student):
    for key, value in student.items():
        print(key, ":", value)


print_items(student)


# Dictionary + Condition
def check_result(student):
    score = student["score"]

    if score >= 40:
        return "Pass"
    else:
        return "Fail"


result = check_result(student)
print(result)


# Multiple return values + tuple unpacking
def analyse_student(student):
    name = student["name"]
    score = student["score"]

    if score >= 40:
        return name, score, "Pass"
    else:
        return name, score, "Fail"


student_name, student_score, result = analyse_student(student)

print("Name:", student_name)
print("Score:", student_score)
print("Result:", result)


# Final Challenge — Dictionary + Function + Conditions
def get_student_summary(student):
    name = student["name"]

    if "score" in student:
        score = student["score"]

        if score >= 80:
            return f"{name} has a good score"
        else:
            return f"{name} needs more practice"
    else:
        return "Score not available"


print(get_student_summary(student))