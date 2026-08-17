students = [
    {"name": "Omar", "score": 85},
    {"name": "Rahim", "score": 72},
    {"name": "Karim", "score": 91},
    {"name": "Sakib", "score": 78},
    {"name": "Nabil", "score": 88}
]


def analyze_students(students):
    count = 0
    name = students[0]["name"]
    highest = students[0]["score"]

    for student in students:
        score = student["score"]
        current_name = student["name"]

        if score > highest:
            highest = score
            name = current_name

        if score >= 40:
            count += 1

    return name, highest, count


student_name, highest_score, passed = analyze_students(students)

print("Highest student:", student_name)
print("Highest score:", highest_score)
print("Passed students:", passed)