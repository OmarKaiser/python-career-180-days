Day 07 — Python Functions: Practical Practice

Learning Objectives

Create functions with parameters.

Use return to send values back to the caller.

Understand print() vs return.

Chain function calls.

Use functions with lists and loops.

Combine functions with conditions and calculations.

Use accumulator variables.

Return multiple values.

Unpack multiple return values.

Find largest and smallest values without max() or min().

Build functions that perform multiple related calculations.

Understand the purpose of helper functions and code reuse.

Concepts Learned

1. Parameters and Arguments

A parameter is the variable in a function definition.

def greet(name):
    print("Hi,", name)

An argument is the actual value passed when the function is called.

greet("Omar")

Here, name is the parameter and "Omar" is the argument.

2. return vs print()

print() displays a value on the screen.

return sends a value back to the caller so the program can store or use it.

def add(a, b):
    return a + b

result = add(10, 20)

3. Function Chaining

A returned value can become the input of another function.

value
  ↓
square()
  ↓
add_ten()
  ↓
double()

This allows several small operations to be combined.

4. Functions + Lists + Loops

A function can receive a list and process every element using a loop.

Common pattern:

def process_numbers(numbers):
    total = 0

    for number in numbers:
        # process number
        total = total + number

    return total

5. Conditions Inside Functions

Functions can use conditions to process only specific values.

For example:

if number % 2 == 0:

checks whether a number is even.

6. Accumulators

An accumulator stores a value that changes during a loop.

For a total:

total = 0

for number in numbers:
    total = total + number

For a count:

count = 0

for number in numbers:
    if number % 2 == 0:
        count = count + 1

7. Multiple Return Values

A function can return multiple values:

return count, total

They can be unpacked:

even_count, even_total = analyze_even_numbers(numbers)

The values are assigned from left to right.

8. Finding Largest and Smallest Without Built-ins

Largest:

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

Smallest:

smallest = numbers[0]

for number in numbers:
    if number < smallest:
        smallest = number

The initial value must be set before the loop so it is not reset on every iteration.

9. Helper Functions

A helper function is a small, reusable function with a clear responsibility.

The main idea is:

Write code once and reuse it whenever needed.

Breaking a larger problem into smaller functions makes code easier to understand, test, debug, and maintain.

Important Mistakes Corrected

Returning a function instead of its result

Incorrect:

return find_largest

This refers to the function itself.

A function must be called when its result is needed:

find_largest(numbers)

Resetting variables inside a loop

Incorrect:

for number in numbers:
    largest = numbers[0]

Correct:

largest = numbers[0]

for number in numbers:
    if number > largest:
        largest = number

Forgetting to store a calculation

This calculates a value but does not save it:

number * number

This stores the result:

square = number * number

Inconsistent variable names

Use the same parameter name consistently throughout a function.

def analyze_numbers(numbers):
    largest = numbers[0]

    for number in numbers:
        ...

Day 07 Progression

Functions
    ↓
Parameters and arguments
    ↓
Return values
    ↓
Function chaining
    ↓
Functions + lists
    ↓
Functions + loops
    ↓
Functions + conditions
    ↓
Accumulators
    ↓
Multiple return values
    ↓
Tuple unpacking
    ↓
Largest / smallest algorithms
    ↓
Combined analysis
    ↓
Helper-function concept

Day 07 Status

Completed

The exercises were consolidated to remove repeated practice that tested the same algorithm without introducing a new concept.