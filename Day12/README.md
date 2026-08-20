# Day 12 - Variable-Length Arguments

## Topics Covered

- `*args`
- `**kwargs`
- Variable-length positional arguments
- Variable-length keyword arguments
- Using `*args` and `**kwargs` together
- Iterating through keyword arguments with `.items()`
- Safely accessing optional dictionary values with `.get()`

## `*args`

`*args` allows a function to accept any number of positional arguments.

```python
def add_numbers(*args):
    print(args)

add_numbers(10, 20, 30)