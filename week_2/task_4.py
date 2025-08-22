
#   Number 1
quote = input("Enter your favorite quote: ")
print(quote)
title = ("quote")
print("\"" + quote.title() + "\"")

#or
# favorite quote
quote = input("Enter your favorite life quote: ")

# Convert to title case
quote_title_case = quote.title()

# Print with quotation marks using escape sequences
print("Your favorite quote is: \"" + quote_title_case + "\"")


#   Number 2
empty_list = []
print(empty_list)
items_1 = input("Enter First items you preffed: ")
item_2 = input("Enter second item of your choice: ")
item_3 = input("Enter the last item of your choice: ")
shopping_items = (items_1, item_2, item_3)
print(shopping_items)
#or
# Create an empty list
shopping_list = []

# 3 shopping items one by one
for i in range(3):
    item = input(f"Enter item {i+1}: ")
    shopping_list.append(item)

# Display the list as a single string separated by commas
print("Your shopping list: " + ", ".join(shopping_list))


# Number 3
sentence = input("Write a simple sentence: ")
print(len(sentence))

#or
# Ask the user for a sentence
sentence = input("Enter a sentence: ")

# Split the sentence into a list of words
words = sentence.split()

# Print how many words are in the sentence
print(f"Your sentence contains {len(words)} words.")

#  Number 4
# Ask the user to enter 5 names separated by spaces
names_input = input("Enter 5 names separated by spaces: ")

# Convert all names to lowercase and split into a list
names_list = names_input.lower().split()

# Sort the list alphabetically
names_list.sort()

# Display them one name per line
print("\nSorted Names:")
for name in names_list:
    print(name)

#   Number 5
# Create empty lists
student_names = []
student_scores = []

# Ask for 3 student names and their scores
for i in range(3):
    name = input(f"Enter name of student {i+1}: ")
    score = float(input(f"Enter score for {name}: "))
    
    # Store in respective lists
    student_names.append(name)
    student_scores.append(score)

# Print formatted output
print("\n--- STUDENT SCORES ---")
print(f"{'Name':<15}{'Score':>10}")
print("-" * 25)
for i in range(3):
    print(f"{student_names[i]:<15}{student_scores[i]:>10.2f}")

#   Number 6
# Ask the user to input a word
word = input("Enter a word: ")

# Print the length of the word
print(f"Length of the word: {len(word)}")

# Check case type
if word.isupper():
    print("The word is in UPPERCASE.")
elif word.islower():
    print("The word is in lowercase.")
elif word.istitle():
    print("The word is in Title Case.")
else:
    print("The word has a mix of cases.")

# Reverse the word using slicing
reversed_word = word[::-1]
print(f"Reversed word: {reversed_word}")

#   Number 7
# Create a list of five cities
cities = ["Lagos", "Abuja", "Kano", "Ibadan", "Enugu"]

# Replace the third city with a new one entered by the user
new_city = input("Enter a new city to replace the third city: ")
cities[2] = new_city

# Remove the last city
cities.pop()

# Add a new city to the beginning of the list
first_city = input("Enter a city to add at the beginning: ")
cities.insert(0, first_city)

# Print the updated list
print("\nUpdated list of cities:", cities)


