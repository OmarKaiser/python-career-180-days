# Day 11: Functions and Arguments Practice


def calculate_total(price, tax=0.10):
    return price + price * tax


def introduce(name, age, city):
    print(name, age, city)


def greet(name, message="Hello"):
    print(message, name)


def profile(name, age=25, city="Dhaka"):
    print(name, age, city)


def order(item, quantity=1, priority="Normal"):
    print(item, quantity, priority)


# Positional arguments
print(calculate_total(100))

# Keyword arguments
introduce(city="Dhaka", name="Omar", age=25)

# Default argument overridden with a keyword argument
greet(name="Omar", message="Welcome")

# Mixing positional and keyword arguments
greet("Omar", message="Hi")

# Using default and keyword arguments
profile("Omar", age=30)
profile("Omar", city="Chittagong")

# Another example
order("Laptop", priority="High")