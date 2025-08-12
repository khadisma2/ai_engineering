# Uppercase
name = "my name is Ismail Rasaki"
print(name.upper())

#Lower
sentence = "Ismail is the master of python programming"
print(sentence.lower())

#Title
sentence = "Ismail is the master of python programming"
print(sentence.title())

# Strip
text = "    Abuja   "
print(text.strip())

# Replace
message = "I love Java"
print(message.replace("Java", "Python"))

# Swapcase
text = "hello ABEOKUTA"
print(text.swapcase())

# Lstrip
text = "    Nigeria"
print(text.lstrip())

#   Rstrip
text = "Nigeria     "
print(text.rstrip())

# Split
fruits = "mango orange banana"
print(fruits.split())

#   Rsplit
text = "one,two,three,four,five"
print(text.rsplit(",", 3))

# splitlines
lines = "I love Ade\nAde is my love\nHe loves his Mum"
print(lines.splitlines()
      )

#   Join
words = ["I",   "love", "programming"]
print(" ".join(words))

#   Center
text = "Python"
print(text.center(20, "-"))

#   ljust
text = "Python"
print(text.ljust(10, "*"))

#   rjust
text = "Python"
print(text.rjust(10, "*"))

#   Z Fill
num = "42"
print(num.zfill(5))
print(num.zfill(9))
print(num.zfill(100))

#   isalpha
print("Lagos".isalpha())
print("Lagos123".isalpha())
print("LagosAbeokuta".isalpha())

#   isdigit
print("123456".isdigit())

#   isalnum
print("pyhton123".isalnum())
print("Python 123".isalnum())

