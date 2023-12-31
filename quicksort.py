import statistics
import random


def quicksort(numbers):
    if len(numbers) <= 1:
        return numbers
    else:
        pivot = statistics.median(
            [
                numbers[0],
                numbers[len(numbers) // 2],
                numbers[-1]
            ]
        )
        items_less, pivot_items, items_greater = (
            [n for n in numbers if n < pivot],
            [n for n in numbers if n == pivot],
            [n for n in numbers if n > pivot]
        )
        print(f"item less: {items_less}")
        print(f"item pivot: {pivot_items}")
        print(f"item greater: {items_greater}")
        return (
                quicksort(items_less) +
                pivot_items +
                quicksort(items_greater)
        )

'''
    This is what each section of quicksort() is doing:

    The base cases where the list is either empty or has only a single element
    Calculation of the pivot item by the median-of-three method
    Creation of the three partition lists
    Recursive sorting and reassembly of the partition lists

'''

# Base cases
print(quicksort([]))
print(quicksort([42]))

# Recursive cases
print(quicksort([5, 2, 6, 1, 3]))
print(quicksort([10, -3, 21, 6, -8]))



def get_random_numbers(length, minimum=1, maximum=100):
    numbers = []
    for _ in range(length):
        numbers.append(random.randint(minimum, maximum))

    return numbers


numbers = get_random_numbers(15, -50, 50)
print(numbers)
print(quicksort(numbers))


