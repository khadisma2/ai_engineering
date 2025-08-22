#   Numbner 1
dish1 = input("Enter your favourite dish 1: ")
dish2 = input("Enter your favourite dish 2: ")
dish3 = input("Enter your favorite dish 3: ")
dish = (dish1, dish2, dish3)
dishes = tuple(dish)
print(dishes)
print(f"{dish1}\n {dish2}\n {dish3}")

#   Number 2
names = input("Enter 5 best friends' names: ")
friends_name = tuple(names)
reversed_name = friends_name[::-1]
print(reversed_name)
print(f"Reversed name: {reversed_name}")

#   Number 3
state = ["Abeokuta", "Lagos", "Kano", "Katsina", "Oyo"]
states = tuple(state)
print(states[0::4])
print("Lagos" in state)
print(len(states))
