#1 Import the whole module
import math
print(math.sqrt(64))
print(math.pi)
print(math.factorial(5))
print(math.log(100, 10))

#2 Import as an alias
import math as m    
print(m.sqrt(81))
print(m.pi)
print(m.factorial(4))

#3 Specific function or variable
from math import sqrt, pi, factorial
print(sqrt(49))
print(pi)
print(factorial(6))
print(factorial(0))

# my_module/first.py
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."
    
# my_module/second.py
def greet(name):
    return f"Hello, {name}! I am creating my own module"

def reverse_string(string):
    return string[::-1]

def count_characters(string):
    return len(string)

def count_words(string):
    return len(string.split())

# my_module/main.py
import first
import second

print("=== Math Functions ===")
print("5 + 3 =", first.add(5, 3))




