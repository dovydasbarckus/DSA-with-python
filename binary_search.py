

#search elements by value and return their index:
def find_index1(elements, value):
    left, right = 0, len(elements) - 1

    while left <= right:
        middle = (left + right) // 2

        if elements[middle] == value:
            return middle

        if elements[middle] < value:
            left = middle + 1
        elif elements[middle] > value:
            right = middle - 1

numbers1 = [5, 6, 7, 8, 9]
print(find_index1(numbers1, 9))


#Searching by key
def find_index2(elements, value, key):
    left, right = 0, len(elements) - 1

    while left <= right:
        middle = (left + right) // 2
        middle_element = key(elements[middle])

        if middle_element == value:
            return middle

        if middle_element < value:
            left = middle + 1
        elif middle_element > value:
            right = middle - 1


fruits = ['orange', 'plum', 'watermelon', 'apple']
fruits.sort(key=len)
print(fruits)

print(find_index2(fruits, key=len, value=6))



#                   binary search with classes
# one variant how to define ordering with classes
from dataclasses import dataclass
@dataclass(order=True)
class Person:
    name: str
    surname: str

# second variant how to define ordering with classes
# from collections import namedtuple
# Person = namedtuple('Person', 'name surname')


people = [
    Person('Bob', 'Williams'),
    Person('John', 'Doe'),
    Person('Paul', 'Brown'),
    Person('Alice', 'Smith'),
    Person('John', 'Smith'),
]


from operator import attrgetter
by_surname = attrgetter('surname')
people.sort(key=by_surname)
print(people)


def find(elements, value, key):
    left, right = 0, len(elements) - 1

    while left <= right:
        middle = (left + right) // 2
        middle_element = key(elements[middle])

        if middle_element == value:
            return middle

        if middle_element < value:
            left = middle + 1
        elif middle_element > value:
            right = middle - 1

founded = find(people, key=by_surname, value='Smith')
print(founded)

