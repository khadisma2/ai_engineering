# Electricity Bill
full_name = input("Enter Customer's full name: ")
units_consumed = int(input("Number of units consumed: "))
cost_per_unit = float(input("Cost Per Unit: "))
total_bill = units_consumed * cost_per_unit
good_bye = "Thanks for your patronage"
print("\n+++++++ KHADISMA ELECTRICITY BILL RECEIPT ++++++++")
print(f"Customer's Full name:\t{full_name}\nNumber of Units Consumed\t{units_consumed}\nCost Per Units:\t{cost_per_unit}\nTotal Bill:\t{total_bill}")
print("Thanks for your patronage")
print("++++++++++++++++++++++++++++++++++++++++++")


# 2nd Method
full_name = input("Enter customer's full name: ")
units_consumed = int(input("Enter units consumed (kWh): "))
cost_per_unit = float(input("Enter cost per unit (₦): "))
total_bill = units_consumed * cost_per_unit

# Print a neatly formatted receipt using escape sequences
print("\n--- ELECTRICITY BILL RECEIPT ---")
print(f"Customer Name:\t{full_name}")
print(f"Units Consumed:\t{units_consumed} kWh")
print(f"Cost per Unit:\t₦{cost_per_unit:,.2f}")
print(f"Total Bill:\t₦{total_bill:,.2f}")
print("-------------------------------")
