print("Welcome to my class")
print("Let's learn Python together!")
print("Python is fun and powerful.")
print("Let's start coding!")

# Print with variable
name = "Ismail"
age = 25
date_of_birth = "1998-01-01"
print("Name:", name)
print("Age:", age)
print("Date of Birth:", date_of_birth)  

# Using f-strings with print()
name = "Aremu"
age = 45
date_of_birth = "1990-01-01"
score = 95  
print(f"my middle name is {name} i am age {age} years old. my date of birth {date_of_birth} i scored {score} in the Exam.")

# Using string concatenation
first_name = "Ismail"   
middle_name = "Aremu"
last_name = "RASAKI"
print("Full name: " + first_name + " " + middle_name + " " + last_name)

# Using Comma vs concatenation
print("Hello", "World")  # With Comma   
print("Hello" + " " + "World" + " " + "welcome to my coding class")  # With Concatenation

# Escape sequences in print - "\n", "\t",
print("I love Ade\nI love Python\n")        
print("I love ade\t      i love coding\t")     
print("My baby is 5yrs old\n I love her so much\t Do you like your father\n Do you like your mother?")
print("name\t\tage\tlocation")

print("file path: C:\\Users\\Ismail\\Documents\\Python")
print("file path: https://www.canva.com/design/DAGvBdHyerM/Rek6hTLjbFCiAOFGYucIxg/edit?utm_content=DAGvBdHyerM&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton")

print("I love you\b")

print("\a")

print("Python", "is", "fun", sep=" - ")
print("This is the first line.", end=" ")
print("This is the second line.")

name = input("What is your name: ")
print("Hello,", name)
print("How can i help you,", name)
print("How may i help you?,", name)

age = int(input("How old are you?: " ))
print("How old are you? ")
print("You will be years old next year.")

# Ask the user for a number
age = int(input("Enter your age: "))
print("Enter your age:", age)

# Calculator using input
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
sum_result = num1 + num2
print(f"The sum of {num1} and {num2} is {sum_result}.")