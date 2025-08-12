# Number 1
name = input("Enter your name: ")
print(name.upper())

text_to_convert = input("Please enter text to convert: ")
print(f"Corrected text is {text_to_convert.upper()}")

# Number 2
text = "Python"
print(text[0::5])

word = "python"
print(f"First Letter: {word[0]}, Last Letter {word[-1]}")

# Number 3
name = input("What is your name?: ")
print("Hello!", name)

user_name = input("What is your name? ")
print(f"Hello, !".replace('!', user_name))

# Number 4
word = "Python"
print(word.index("n"))

word_to_count = input("Type text to count: ")
last_character = word_to_count[-1]
print(f"It contains {word_to_count.rindex(last_character) + 1} characters")

# Number 5
message = "Hello World"
print(message.replace("World", "Python Programming and Coding"))

print("Hello World".replace('World', 'Python'))

# Number 6
text_to_check = input("Input Text to check for python(case insensitive): ")
print("True") if 'python' in text_to_check.lower() else print("False")
# also
print('python' in text_to_check.lower())

# Number 7
string_to_reverse = input("Input string to reverse: ")
# for each in reversed(string_to_reverse): 
#     print(each)
list = reversed(string_to_reverse)
print(''.join(list))

# Number 8
string_with_spaces = " I have trailing spaces "
print(string_with_spaces.strip())

# Number 9
sentence = input("Please, enter your sentence: ").lower()
vowel_list = ['a', 'e', 'i', 'o', 'u']
vowel_count = sum(1 for letter in sentence if letter in vowel_list)
print(f"There are {vowel_count} vowels")
vowel_count = sentence.count('a') + sentence.count('e') + sentence.count('i') + sentence.count('o') + sentence.count('u')
print(f"There are {vowel_count} vowels")

# Number 10
string_number = input("Your number to multiply: ")
string_number_converted = int(string_number)
print(f"The answer is: {string_number_converted*2}")

# Number 11
fruit_string = "apple,banana,orange"
fruit_list = fruit_string.split(',')
print(f"Fruit list: {fruit_list}")

# number 12
user_sentence = input("Please input a sentence: ")
sentence_list = user_sentence.split(" ")
print(' \n'.join(sentence_list))

# Number 13
user_string = input("Input your desired string: ")
print(user_string.replace(' ', '~'))

# Number 14
word = "banana"
print(f"Letter 'A' appears {word.lower().count('a')} times")

# Number 15
url = input("Please input valid url(https://): ")
print(url.startswith("https://"))
