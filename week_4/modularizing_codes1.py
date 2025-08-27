# #   modularizing_codes
# #   1. Range()
# for i in range(5):
#     print(i)    # 0,1,2,3,4

# #   Zip ()
# digit = [1,2,3]
# names = ['Alice', 'Bob', 'Charlie']
# ages = [25, 30, 35] 
# scores = [85, 90, 88]
# for d, n, a, s in zip(digit, names, ages, scores):
#     print(d, n, a, "scored", s )

# #   Map()
# nums = [1, 2, 3, 4, 5]
# squared = list(map(lambda x: x**2, nums))
# print(squared)

# #   Filter()
# even_nums = list(filter(lambda x: x % 2 == 0, nums))
# print(even_nums)

# #   Students Performance & Feedback System
# #   1. Input()Student Data
# name1 = input("Enter first student name: ")
# score1 = int(input("Enter score for " + name1 + ": "))

# name2 = input("Enter second student name: ")
# score2 = int(input("Enter score for " + name2 + ": "))

# name3 = input("Enter third student name: ")
# score3 = int(input("Enter score for " + name3 + ": "))

# #  2: store data in lists
# names = [name1, name2, name3]
# scores = [score1, score2, score3]

# # 3: Display Data
# print("\nStudent Data:")
# for index, (n, s) in enumerate(zip(names, scores)):
#     print(f"{index + 1}. {n} - {s}")

# # 4: Summary using built-ins
# total = sum(scores)
# average = round(total / len(scores), 2)
# highest = max(scores)
# lowest = min(scores)

# print("\nPerformance Summary:")
# print("Total Score:", total)
# print("Average Score:", average)
# print("Highest Score:", highest)
# print("Lowest Score:", lowest)

# #   5: Ranking (using sorted and zip)
# ranked = sorted(zip(scores, names), reverse=True)
# print("\nRanking:")
# for rank, (score, name) in enumerate(ranked, 1):
#     print(f"{rank}. {name} - {score}")

# # 6: Check Data Types
# print("\nData Type Checks:")
# print("Type of names:", type(names))
# print("Type of Scores:", type(scores))
# print("ID of names list:", id(names))
# print("ID of scores list:", id(scores))

# #   7: Filter Passing Students (score >= 50)
# passing = list(filter(lambda s: s >= 50, scores,))
# print("\npassing Scores:", passing)

# # 8: Map names to uppercase
# upper_names = list(map(lambda n: n.upper(), names))
# print("Uppercase Names:", upper_names)

# # 9: Use Help() to show documentation of len
# print("\nHelp on len():")
# help(len)

# #   Function Arguments and Parameters
# # 1. Defining a Function
def greet():
     print("Hello, welcome to the Student Performance System!")
greet()
greet()
greet()

#   Function with an argument - the placeholder
def greet(name):
    print("Hello", name, "welcome to the Student Performance System!")
greet("Ismail")
greet("ISmail RASAKI")

def greet(name):
     print("Hello", name)

#   Function Call
result = greet("Alice")
print("Result:", result)  # Output: Result: None)

def add(a, b):
    return a + b
result = add(4, 6)
print("The sum is:", result)  # Output: The sum is: 10

def multiply(a, b):
    return a * b    
result = multiply(4, 6)
print("The product is:", result)  # Output: The product is: 24

#   Yield
def count_up_to(n)
    i = 1
    while i <= n:
        yield i
        i += 1
for number in count_up_to(5):
    print(number)  # Output: 1, 2, 3, 4, 5

def introduce(name, track):
        print("My name is", name)
        print("I am learning", track, ".")
introduce("Ngozi", "AI Developer")
introduce("AI Developer", "Ngozi")
