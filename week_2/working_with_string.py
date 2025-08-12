#Single Quote
name = 'Ismail'

# Double Quote
greeting = "Hello"

# Tripple quote
story = '''once upon a time, there was a coder named Ismail'''
peom = """Love is sweet with a truthful partner"""

# String with numbers and symbols
password = "p@ssw0rd123"

# Indexing
word = "Python"
print(word[0])  # P
print(word[-1]) # n
print(word[2])  #t
print(word[-3])  #h
print(word[-5])  #y

# Slicing
word = "Python"
print(word[1:5])    #ytho
print(word[:3])     #pyt
print(word[::-2])   #nhy
print(word[::2])    #pto

#Concatenation
a = "Hello"
b = "World"
print(a + " " + b)

a = "I"
b = "love"
c = "you"
print(a + " " + b + " " + c)

# Repetition
word = "Hi"
print(word * 3)

word = "Thank you!"
print(word * 5)

# Membership
text = "Python programming"
print("Python" in text)
print("Java" in text)

# find()/ rfind()
text = "Hello World"
print(text.find("0"))
print(text.rfind("0"))

# Index() / rindex()
text = "Hello World"
print(text.index("World"))

# Start with () / endswith()
filename = "data.csv"
print(filename.startswith("data"))
print(filename.endswith(".csv"))



