import random
from timed_func import timed_func

# Optimized Bubble sort in Python

@timed_func
def bubbleSort(array):

    # loop through each element of array
    for i in range(len(array)):
        print(i)
        # keep track of swapping
        swapped = False

        # loop to compare array elements
        for j in range(0, len(array) - i - 1):
            print(array)
            # compare two adjacent elements
            # change > to < to sort in descending order
            if array[j] > array[j + 1]:

                # swapping occurs if elements
                # are not in the intended order
                temp = array[j]
                array[j] = array[j + 1]
                array[j + 1] = temp

                swapped = True

        # no swapping means the array is already sorted
        # so no need for further comparison
        if not swapped:
            break
    return array

# data = [-2, 45, 0, 11, -9]
# bubbleSort(data)
# print('Sorted Array in Ascending Order:')
# print(data)

data2 = [random.randint(1,100) for i in range(100)]
print(bubbleSort(data2))



