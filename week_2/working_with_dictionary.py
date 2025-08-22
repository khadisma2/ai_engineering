# #   Synax
# #   dictionary_name = {key1: value1, key2: value2, ...}
# #   Creating Dictionary Using Curly braces
# student = {
#     "name": "Ismail",
#     "age" : 20, 
#     "course" : "AI Engineering"
# }
# print(student)

# #   Using the dict() constructor
# student_info = dict(name="Ismail", age=20, course="AI Engineering")
# print(student_info)

# #   Empty Dictionary
# empty_dict = {}
# print(empty_dict)

# #   Syntax
# #   {key_expression: value_expression for item in iterable if condition}
# #   Create a dictionaryn of numbers and thier squares
# squares = {x: x**2 for x in range(1, 16)}
# print(squares)

# #   With condition
# #   Dict of Even nmubers
# even_cubes = {x: x**3 for x in range(1, 16) if x % 2 == 0}
# print(even_cubes)   

# #   From Existing dictiionary
# students = {"Ismail": 94, "Rasaki": 45, "Aisha": 89, "Ola": 38}
# #   Filter students who passed (score >= 50)
# passed_students = {name: score for name, score in students.items() if score >= 50}
# print(passed_students)

# #   Using string as keys
# names = ["Ismail", "Rasaki", "Aisha", "Ola"]
# lenghts = {name: len(name) for name in names}
# print(lenghts)

#   Define a dictionary
student = {"name": "Ismail", "age": 20, "course": "AI Engineering"}
print(student["name"])
print(student.get("age"))
print(student.get("course", "Course not found"))  # Default value if key not found
print(student.get("grade", "Grade not found"))  # Key not found, returns default message

# Using pop()
student.pop("age")  # Removes the key "age" and returns its value
del student["course"]
student.clear()
print(student)

# Dictionary Methods
# dot keys(), dot values(), dot items(), dot update(), dot popitem(), dot copy()
person = {"name": "Ismail", "age": 32}
print(person.keys())   # Returns a view of the keys
print(person.values()) # Returns a view of the values
print(person.items())  # Returns a view of the key-value pairs
person.update({"city": "Lagos", "country": "Nigeria"})  # Adds new key-value pairs
print(person)

# Nested Dictionaries
students = {
    "Ismail": {"age": 20, "course": "AI Engineering"},
    "Rasaki": {"age": 22, "course": "Data Science"},
    "Aisha": {"age": 21, "course": "Web Development"}
}
print(students["Ismail"]["course"])  # Accessing nested dictionary
print(students.get("Rasaki", {}).get("age", "Age not found"))   # Safely accessing nested dictionary with default value

# Looping throuigh dictionaries (keys, value, key-values)
student = {"name": "Ismail", "age": 20, "course": "AI Engineering"}
for key, value in student.items():
    print(key)
    print(value)
    print(f"{key}: {value}")  # Formatted string for better readability"},

# Storing a students bio data
student = {
    "name": "Ismail",
    "age" : 20,
    "course" : "AI Engineering",    
    "subjects" : ["Python", "AI", "Data Science"],
    "grades" : {"Python": "A", "AI": "B", "Data Science": "A"},
    "is_full_time" : True}
print(f"Name: {student['name']}")
print(f"subjects: {', '.join(student['subjects'])}")
print(f"Grades: {', '.join([f'{sub}: {grade}' for sub, grade in student['grades'].items()])}")
print(f"Full-time student: {'Yes' if student['is_full_time'] else 'No'}")
