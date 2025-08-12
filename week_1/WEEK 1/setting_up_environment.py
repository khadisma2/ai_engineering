# Basic usage of print()
print("hello world")
print("welcome to the world of Python programming")

# Using print() with variables
name = "ismail"
age = 25
print("Name:", name)
print("Age:", age)

# Using f-strings with print()
name = "Aremu"
score = 95
print(f"{name} scored {score} in the Exam.")

# Using string concatenation
first_name = "Ismail"
last_name = "RASAKI"
print("Full name: " + first_name + " " + last_name)

# Using Comma vs concatenation
print("Hello", "World")  # With Comma
print("Hello" + " " + "World")  # With Concatenation

#Escape sequences in print - "\n", "\t",
print("line1\nline2")               # New line
print("Item1\tItem2")               # Tab space
print('It\'s a PYTHON!')             # Single quote

#Newline (\n)
print("Welcome to Python\nProgramming World")

#Tab (\t)
print("Name:\tIsmail\nAge:\t25")
print("Ismail\tRasaki\nPython\tAIENgineer")

#Quotes inside strings
print("He said, \"Python is great!\"")
print('It\'s a beautiful day!')

# Backslash
print("File path: C:\\Users\\Ismail\\Documents\\Python")

#printing pyramid
print(
    "    *\n"
    "   ***\n"
    "  *****\n"
    " *******\n"
    "*********\n"
)
print(
    "    *\n"
    "   ***\n"
    "  *****\n"
    " *******\n"
    "*********\n"
)
'\t'

# printing a triangle
print(
    "    *\n"
    "   ***\n"
    "  *****\n"
    " *******\n"
    "*********\n"
)   
#print a square
print(  "*********\n"
    "*       *\n"
    "*       *\n"
    "*       *\n"
    "*********\n"
)   
# printing a rectangle
print(              
    "*********\n"
    "*       *\n"
    "*       *\n"
    "*       *\n"
    "*       *\n"
    "*********\n"
)       
# Printing a diamond shape
print(  
    "    *\n"
    "   ***\n"
    "  *****\n"
    " *******\n"
    "*********\n"
    " *******\n"
    "  *****\n"
    "   ***\n"
    "    *\n"
)   
print("AAAAAAAAAAA\n AAAAAAAAA\n  AAAAAAA\n   AAAAA\n    AAA\n     A\n")

print("AAAAAAAAAAA\n AAAAAAAAA\n  AAAAAAA\n   AAAAA\n    AAA\n     A\n     R\n    RRR\n   RRRRR\n  RRRRRRR\n RRRRRRRRR\n")
# Carriage Return (\r)
print("123456\rABC")        # Output: ABC456 (replace 123)

#Backspace (\b)
print("Hello\bWorld")  # Output: HellWorld

#Bell/alert (may or may not beep depending on the environment)
print("\a") # Triggers a bell sound (if supported)

