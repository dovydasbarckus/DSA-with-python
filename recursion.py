from timeit import timeit


setup_string = """
print("Recursive:")
def factorial(n):
    return 1 if n <= 1 else n * factorial(n - 1)
"""
print(timeit("factorial(4)", setup=setup_string, number=10000000))

setup_string = """
print("Iterative:")
def factorial(n):
    return_value = 1
    for i in range(2, n + 1):
        return_value *= i
    return return_value
"""
print(timeit("factorial(4)", setup=setup_string, number=10000000))



setup_string = """
from functools import reduce
print("reduce():")
def factorial(n):
    return reduce(lambda x, y: x * y, range(1, n + 1) or [1])
"""
print(timeit("factorial(4)", setup=setup_string, number=10000000))



setup_string = """
from math import factorial
print("using math model factorial:")
"""

print(timeit("factorial(4)", setup=setup_string, number=10000000))




#  traversed list with recursion
names = [
    "Adam",
    [
        "Bob",
        [
            "Chet",
            "Cat",
        ],
        "Barb",
        "Bert"
    ],
    "Alex",
    [
        "Bea",
        "Bill"
    ],
    "Ann"
]

def count_leaf_items(item_list):
    """Recursively counts and returns the
       number of leaf items in a (potentially
       nested) list.
    """
    print(f"List: {item_list}")
    count = 0
    for item in item_list:
        if isinstance(item, list):
            count += count_leaf_items(item)
        else:
            print(f"Counted leaf item \"{item}\"")
            count += 1

    print(f"-> Returning count {count}")
    return count

count_leaf_items(names)


from functools import lru_cache
@lru_cache(maxsize=100)
def fibonacci_recursive(n):
    print("Calculating F", "(", n, ")", sep="", end=", ")

    # Base case
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive case
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

print(fibonacci_recursive(5))