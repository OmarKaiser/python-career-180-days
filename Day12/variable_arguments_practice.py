# Day 12: Variable-Length Arguments

# 1. *args - accepts any number of positional arguments
def add_numbers(*args):
    total = 0

    for number in args:
        total += number

    return total


print("Sum:", add_numbers(10, 20, 30))


# 2. **kwargs - accepts any number of keyword arguments
def print_profile(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)


print_profile(name="Omar", age=29, city="Dhaka")


# 3. Using *args and **kwargs together
def show_data(*args, **kwargs):
    print("Numbers:", args)
    print("Details:", kwargs)


show_data(10, 20, 30, name="Omar", city="Dhaka")


# 4. Independent practice
def user_summary(*skills, **details):
    print("Skills:", skills)
    print("Details:", details)


user_summary(
    "Python",
    "SQL",
    "Machine Learning",
    name="Omar",
    city="Dhaka"
)