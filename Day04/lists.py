# Exercise 1: Create and access a list

numbers = [10, 20, 30, 40, 50]

print(numbers)
print(numbers[0])
print(numbers[-1])


# Exercise 2: Modify and add elements

numbers = [10, 20, 30, 40, 50]

numbers[1] = 25
numbers[4] = 55
numbers.append(60)
numbers.append(70)

print(numbers)


# Exercise 3: Loop through a list

numbers = [10, 20, 30, 40, 50]

for number in numbers:
    print(number)


# Exercise 4: Print even numbers

numbers = [10, 15, 20, 25, 30, 35, 40]

for number in numbers:
    if number % 2 == 0:
        print(number)


# Exercise 5: Count and sum even numbers

numbers = [10, 15, 20, 25, 30, 35, 40]

count = 0
total = 0

for number in numbers:
    if number % 2 == 0:
        count = count + 1
        total = total + number

print("Count:", count)
print("Total:", total)


# Exercise 6: Count even numbers, sum even numbers,
# and sum all numbers

numerical_numbers = [3, 7, 10, 12, 15, 20]

count = 0
total = 0
all_total = 0

for number in numerical_numbers:
    all_total = all_total + number

    if number % 2 == 0:
        count = count + 1
        total = total + number

print("Count:", count)
print("Total Even:", total)
print("ALL Total:", all_total)