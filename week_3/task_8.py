#   Number 1
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"{num1} == {num2} : {num1 == num2}")
print(f"{num1} != {num2} : {num1 != num2}")
print(f"{num1} > {num2} : {num1 > num2}")
print(f"{num1} < {num2} : {num1 < num2}")

# Answers 1
#   4 == 5 : False because 4 is not equal to 5
#   4 != 5 : True because 4 is not equal to 5
#   4 > 5 : False because 4 is not greater than 5
#   4 < 5 : True because 4 is less than 5   

#  Number 2
name = input("Enter your name: ")
age = int(input("Enter your age: "))
score = int(input("Enter your test score: "))
eligibility = (age < 18) and (score > 70)
print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")

# Answers 2  
#   This program collects a candidate's personal details (name, age, and score) and checks their eligibility based on two conditions:
#1. The candidate must be younger than 18 years.
#2. The candidate's test score must be greater than 70.
#3. It then prints the candidate's details along with their eligibility status.

# Ask the user for their name
name = input("Enter your name: ")

# Ask for age and convert it to an integer
age = int(input("Enter your age: "))

# Ask for test score and convert it to an integer
score = int(input("Enter your test score: "))

# Determine eligibility:
# Candidate must be below 18 years old AND have a score greater than 70
eligibility = (age < 18) and (score > 70)

# Display results in a formatted manner
print(f"Candidate: {name}\nAge: {age}\nScore: {score}\nEligible: {eligibility}")

# Collect applicant details
name = input("Enter your full name: ")
citizenship = input("Are you a Nigerian citizen? (yes/no): ").strip().lower()
enrollment = input("Are you a registered full-time undergraduate in a Nigerian university? (yes/no): ").strip().lower()
other_scholarship = input("Are you currently on any Oil & Gas scholarship? (yes/no): ").strip().lower()

# Ask for number of WAEC distinctions (A or B grades, including English & Maths)
waec_distinctions = int(input("Enter number of WAEC distinctions (A or B, including English & Maths): "))

# Eligibility conditions
is_nigerian = (citizenship == "yes")
is_enrolled = (enrollment == "yes")
no_other_scholarship = (other_scholarship == "no")
good_waec = (waec_distinctions >= 5)

# Final eligibility check
eligibility = is_nigerian and is_enrolled and no_other_scholarship and good_waec

# Display summary
print("\n=== Federal Government Scholarship Eligibility Check ===")
print(f"Candidate: {name}")
print(f"Citizenship: {citizenship.capitalize()}")
print(f"Enrolled in Nigerian University: {enrollment.capitalize()}")
print(f"Receiving Other Oil & Gas Scholarship: {other_scholarship.capitalize()}")
print(f"WAEC Distinctions: {waec_distinctions}")
print(f"Eligibility Status: {'✅ Eligible' if eligibility else '❌ Not Eligible'}")

#   Number 3
# List of items available in the store
items = ["Book", "Pen", "Bag", "Pencil", "Drawing Book", "Sock"]
# Corresponding prices of the items
prices = [500, 100, 2000, 50, 1500, 300]
# Start with an empty cart total
cart_total = 0
# Add prices of some items into the cart
cart_total += prices[0]   # Book
cart_total += prices[1]   # Pen

print(f"Total Price: ₦{cart_total}")

#   Number 4
# Create an empty dictionary
student = {}

# Ask the user for name and age
student["name"] = input("Enter your name: ")
student["age"] = int(input("Enter your age: "))

# Add a list of scores
student["scores"] = [70, 85, 90]

# Check if student has passed (average score >= 50)
average_score = sum(student["scores"]) / len(student["scores"])
student["passed"] = average_score >= 50

# Check if student is a teenager (age between 13 and 19)
student["teenager"] = (student["age"] >= 13) and (student["age"] <= 19)

# Print student record
print("\nStudent Record:")
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"Scores: {student['scores']}")
print(f"Passed: {student['passed']}")
print(f"Teenager: {student['teenager']}")

#   Number 5
# Create a dictionary with items and their quantities
store = {"Book": 10, "Pen": 20, "Bag": 5}

# Print store before purchase
print(f"Before purchase: {store}")

# Ask the user for the item and quantity they want to buy
item = input("Enter the item you want to buy (Book, Pen, Bag): ")
quantity = int(input("Enter the quantity you want to buy: "))

# Check if the item exists in the store and if enough stock is available
if item in store and quantity <= store[item]:
    store[item] -= quantity   # reduce stock using -=
    print(f"After purchase: {store}")
else:
    print("Sorry, item not available or insufficient stock.")

#   Number 6
#   UNILAG Admission Eligibility Checker
# Step 1: Collect candidate details
name = input("Enter your full name: ")
age = int(input("Enter your age: "))
utme_score = int(input("Enter your UTME score: "))
first_choice = input("Is UNILAG your first choice? (yes/no): ").strip().lower()

# Step 2: O'Level requirements
olevel_credits = int(input("Enter the number of O'Level credits you obtained in one sitting: "))
english = input("Do you have credit in English Language? (yes/no): ").strip().lower()
math = input("Do you have credit in Mathematics? (yes/no): ").strip().lower()

# Step 3: Post-UTME score
post_utme_score = int(input("Enter your Post-UTME score: "))

# Step 4: Departmental cut-off (set by UNILAG after Post-UTME, between 200 and 320)
dept_cutoff = int(input("Enter your departmental cut-off mark (between 200 - 320): "))

# ---------------- Eligibility Checks ----------------
eligible = True
reasons = []  # To store reasons for ineligibility

# Age check
if age < 16:
    eligible = False
    reasons.append("You must be at least 16 years old.")

# UTME check
if utme_score < 200:
    eligible = False
    reasons.append("Your UTME score is below 200 (minimum required).")

# First choice check
if first_choice != "yes":
    eligible = False
    reasons.append("UNILAG must be your first choice.")

# O'Level check
if olevel_credits < 5 or english != "yes" or math != "yes":
    eligible = False
    reasons.append("You must have at least 5 credits at one sitting, including English and Mathematics.")

# Post-UTME & Departmental cutoff check
final_score = (utme_score + post_utme_score) // 2  # Weighted performance (UTME + Post-UTME average)
if final_score < dept_cutoff:
    eligible = False
    reasons.append(f"Your average score ({final_score}) is below the departmental cut-off ({dept_cutoff}).")

# ---------------- Final Decision ----------------
print("\n===== UNILAG Admission Eligibility Result =====")
print(f"Candidate Name: {name}")
print(f"Age: {age}")
print(f"UTME Score: {utme_score}")
print(f"Post-UTME Score: {post_utme_score}")
print(f"Final Average Score: {final_score}")
print(f"Departmental Cut-off: {dept_cutoff}")

if eligible:
    print("\n✅ Congratulations! You are eligible for admission into UNILAG.")
else:
    print("\n❌ Sorry, you are not eligible for admission. Reasons:")
    for reason in reasons:
        print(f"- {reason}")
