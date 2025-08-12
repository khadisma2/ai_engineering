# Print Empty
# Method 1 & 2 Using  square brackets & List () constructor
empty_list = []
print(empty_list)

empty_list2 = list()
print(empty_list2)

# Creating list with initial elements
# list of intergers
numbers = [1, 2, 3, 4, 5]
digits = list("678910")
print(numbers)
print(digits)

#   List of strings
fruits = ["apple", "banana", "cheery"]
fruits2 = ["orange, guava, watermelon, papaya"]
print(fruits2)
print(fruits)

#   Mixed Data types
mixed_list = ["Alice", 25, 5.8, True]
print(mixed_list)

come = list("programming")
print(come)

go = list('python')
print(go)

#   Turple
my_turple = (10, 20, 30)
list_from_turple = list(my_turple)
print(list_from_turple)

#   Range
number_range = list(range(5))
print(number_range)

#   List Comprehension
#   Squares of Numbers
squares = [x**2 for x in range(5)]
print(squares)

#   Even Numbers between 0-10
evens = [x for x in range(11) if x % 2 == 0]
print(evens)

#   Nested list
#   Matrix 
matrix  = [[1, 2], [3, 4], [5, 6]]
print(matrix)

#   Accessing elements in a nested list
print(matrix[0])
print(matrix[2])
print(matrix[1])
print(matrix[0][1])

fruits = ["mango", "orange", "banana"]
print(fruits)       # ['mango', 'orange', 'banana']
print(fruits[0])    # mango (first element)
print(fruits[2])    # banana (third element)

#   Allows Duplicates
items = ["rice", "beans", "yam", "rice"]
print(items)

#   Mutable
numbers = [1, 2, 3]
numbers[1] = 20
print(numbers)

#   Dynamics
names = ["Ismail"]
names.append("AbdurRahman")
names.append("Khadija")
print(names)