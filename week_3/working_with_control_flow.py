#   Conditional Statements
#   1. Check if statement
age = 20
if age >= 18:
    print("You are eligible to vote")

#   if-else statement
wallet = 400
price = 500
if wallet >= price:
    print("Purchase successful")
else:    
    print("Insufficient balance try again later") 

#   if-elif-else Statement
score = 85
if score >= 70:
    print("Grade A")
elif score >= 50:
    print("Grade B")
else:
    print('Grade C')

#   Nested (placing if inside another if)
age = 19
citizen = True

if age >= 18:
    if citizen:
        print("You can vote")
    else:
        print("You must ba a citizen to vote")
else:
    print("Too young to vote")


#   Loops
#   for loop
fruits = ["Apple", "Banana", "Orange"]
for fruit in fruits:
    print(f"I like {fruit}")

coordinates = (0.34654, -0.48585, 0.57477)
for point in coordinates:
    print(f"Point: {point}")

    




