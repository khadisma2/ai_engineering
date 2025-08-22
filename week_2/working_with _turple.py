#   Using parentheses ()
fruits = ("apple", "banana", "cherry")
print(fruits)

#   Without parentheses(turble packing)
numbers = 1, 2, 3
print(numbers)

#   Single-Item turple
single_item = ("apple",)
print(single_item)
print(type(single_item))

#   Using tuple() constructor
fruits_list = ["apple", "banana", "cherry"]
fruits_tuple = tuple(fruits_list)
print(fruits_tuple)

#   Ordered
colors = ("red", "green", "blue")
print(colors[0])
print(colors[2])
print(colors[-1])

#   Allow Duplicate
numbers = (1, 2, 2, 3, 4)
print(numbers)

#   Mixed data types
mixed = ("apple", 3, True, 5.6)
print(mixed)

#   NEsted tuple
nested = (("a", "b"), (1, 2))
print(nested)

#   Tuple Operations
#1  indexing
fruits = ("apple", "banana", "cherry")
print(fruits[1])
print(fruits[-2])

#2  Slicing
print(fruits[0:2])
print(fruits[1:3])
print(fruits[::-1])

#   Concatenation
tuple1 = (1, 2)
tuple2 = (3, 4)
result = tuple1 + tuple2
print(result)

#   Repetition
nums = (1, 2, 3)
print(nums * 5)

#   Membership
fruits = ("apple", "banana", "cherry")
print("banana" in fruits)
print("grape" in fruits)
print("grape" not in fruits)

#6  iteration
for fruit in fruits:
 print(fruit)

 #  Unpacking tuple
 person = ("John", 25, "Nigeria") 
 name, age, country = person
 print(name)
 print(age)
 print(country)

 #  numbers = (1, 2, 2, 3, 2, 4, 4)
 print(numbers.count(2))
 print(numbers.index(3))

 #  Converting Between List and Tuple
 # Tuple to List
t = (1, 2, 3)
lst = list(t)
lst.append(4)
print(lst) 

# List back to Tuple
t = tuple(lst)
print(t) 

# Built-in Functions with Tuples
nums = (4, 1, 7, 8, 3)

print(len(nums))   
print(max(nums))   
print(min(nums))   
print(sum(nums))
