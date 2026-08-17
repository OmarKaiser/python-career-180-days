# Day 10 — Python Loops & Control Flow

## Overview

Day 10 focused on mastering Python loops and control flow using `range()`, `break`, `continue`, counting, accumulation, and basic problem-solving algorithms.

The goal was to write efficient loops without using built-in functions like `max()`, `min()`, `sum()`, or `len()`.

---

## Topics Covered

- `range(stop)`
- `range(start, stop)`
- `range(start, stop, step)`
- Reverse iteration
- `break`
- `continue`
- Looping through lists
- Counting values
- Summing values
- Highest and lowest value algorithms
- Even and odd counting
- Multiple calculations in a single loop

---

## 1. Using range()

### Basic range

```python
for i in range(5):
    print(i)
```

Output:

```
0
1
2
3
4
```

### Start and Stop

```python
for i in range(2, 7):
    print(i)
```

Output:

```
2
3
4
5
6
```

### Step

```python
for i in range(2, 11, 2):
    print(i)
```

Output:

```
2
4
6
8
10
```

### Reverse range

```python
for i in range(10, 0, -2):
    print(i)
```

Output:

```
10
8
6
4
2
```

---

## 2. break

`break` immediately stops the loop.

```python
for i in range(1, 10):
    if i == 5:
        break
    print(i)
```

Output:

```
1
2
3
4
```

---

## 3. continue

`continue` skips only the current iteration.

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

Output:

```
1
2
4
5
```

---

## 4. Loop Through a List

```python
numbers = [10, 25, 40, 15, 60, 30]

for number in numbers:
    if number > 30:
        print(number)
```

Output:

```
40
60
```

---

## 5. Counting Pattern

```python
numbers = [45, 12, 89, 34, 67, 23, 100, 8]

count = 0

for number in numbers:
    if number % 2 == 0:
        count += 1

print(count)
```

Output:

```
4
```

---

## 6. Accumulation Pattern

```python
numbers = [10, 20, 30, 40, 50]

total = 0

for number in numbers:
    total += number

print(total)
```

Output:

```
150
```

---

## 7. Conditional Sum

```python
numbers = [10, 25, 40, 15, 60, 30]

total = 0

for number in numbers:
    if number > 30:
        total += number

print(total)
```

Output:

```
100
```

---

## 8. Highest Value Algorithm

```python
numbers = [45, 12, 89, 34, 67, 23]

highest = numbers[0]

for number in numbers:
    if number > highest:
        highest = number

print(highest)
```

Output:

```
89
```

---

## 9. Lowest Value Algorithm

```python
numbers = [45, 12, 89, 34, 67, 23]

lowest = numbers[0]

for number in numbers:
    if number < lowest:
        lowest = number

print(lowest)
```

Output:

```
12
```

---

## 10. Final Challenge

```python
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
```

Output:

```
Highest: 100
Lowest: 8
Even: 4
Odd: 4
Total: 378
```

---

## Key Algorithms Learned

### Count

```python
count = 0

for item in items:
    if condition:
        count += 1
```

### Sum

```python
total = 0

for item in items:
    total += item
```

### Maximum

```python
highest = items[0]

for item in items:
    if item > highest:
        highest = item
```

### Minimum

```python
lowest = items[0]

for item in items:
    if item < lowest:
        lowest = item
```

---

## Day 10 Summary

Today introduced the core control-flow patterns that appear repeatedly in Python, data analysis, algorithms, and machine learning preprocessing.

Instead of relying on built-in functions, every solution was implemented manually using loops, conditions, and accumulator variables.

**Status: Completed ✅**