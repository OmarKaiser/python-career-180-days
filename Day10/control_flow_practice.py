# Day 10 — Python Loops & Control Flow

# range()
for i in range(5):
    print(i)

print("-" * 20)

for i in range(2, 7):
    print(i)

print("-" * 20)

for i in range(2, 11, 2):
    print(i)

print("-" * 20)

for i in range(10, 0, -2):
    print(i)

print("-" * 20)

# break
for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("-" * 20)

# continue
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print("-" * 20)

# Loop through list
numbers = [10, 25, 40, 15, 60, 30]

for number in numbers:
    if number > 30:
        print(number)

print("-" * 20)

# Count even numbers
numbers = [45, 12, 89, 34, 67, 23, 100, 8]

even_count = 0

for number in numbers:
    if number % 2 == 0:
        even_count += 1

print("Even:", even_count)

print("-" * 20)

# Sum numbers
numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:
    total += number

print("Total:", total)

print("-" * 20)

# Highest & Lowest
numbers = [45, 12, 89, 34, 67, 23]

highest = numbers[0]
lowest = numbers[0]

for number in numbers:
    if number > highest:
        highest = number

    if number < lowest:
        lowest = number

print("Highest:", highest)
print("Lowest:", lowest)

print("-" * 20)

# Final Challenge
numbers = [45, 12, 89, 34, 67, 23, 100, 8]

total = 0
highest = numbers[0]
lowest = numbers[0]
even_count = 0
odd_count = 0

for number in numbers:
    total += number

    if number > highest:
        highest = number

    if number < lowest:
        lowest = number

    if number % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Highest:", highest)
print("Lowest:", lowest)
print("Even:", even_count)
print("Odd:", odd_count)
print("Total:", total)