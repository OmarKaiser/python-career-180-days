# Day 14: map() and filter() with lambda

# 1. Using map() to double numbers
numbers = [5, 10, 15]

result = map(lambda x: x * 2, numbers)

print("Doubled numbers:", list(result))


# 2. Using map() to add 10
numbers = [1, 5, 10]

result = map(lambda x: x + 10, numbers)

print("After adding 10:", list(result))


# 3. Using map() to square numbers
numbers = [3, 4, 5]

result = map(lambda x: x * x, numbers)

print("Squared numbers:", list(result))


# 4. Using filter() to keep even numbers
numbers = [1, 2, 3, 4, 5, 6]

result = filter(lambda x: x % 2 == 0, numbers)

print("Even numbers:", list(result))


# 5. Using filter() to keep numbers greater than 10
numbers = [5, 10, 15, 20]

result = filter(lambda x: x > 10, numbers)

print("Numbers greater than 10:", list(result))


# 6. Filter first, then map
numbers = [2, 3, 4, 5, 6]

filter_result = filter(lambda x: x > 3, numbers)

map_result = map(lambda x: x * 10, filter_result)

print("Filtered and multiplied:", list(map_result))


# 7. Map first, then filter
numbers = [1, 2, 3, 4, 5]

map_result = map(lambda x: x * 2, numbers)

filter_result = filter(lambda x: x > 5, map_result)

print("Mapped then filtered:", list(filter_result))


# 8. Final practice
numbers = [1, 2, 3, 4, 5, 6]

filter_result = filter(lambda x: x > 2, numbers)

map_result = map(lambda x: x * 3, filter_result)

print("Final result:", list(map_result))