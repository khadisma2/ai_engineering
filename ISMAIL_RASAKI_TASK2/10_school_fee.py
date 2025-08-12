# school name and fees
school_name = input("Enter the school name: ")
tuition_fee = float(input("Enter the tuition fee (₦): "))
hostel_fee = float(input("Enter the hostel fee (₦): "))
feeding_fee = float(input("Enter the feeding fee (₦): "))
total_fee = tuition_fee + hostel_fee + feeding_fee

# Print receipt format
print("\n--- SCHOOL FEES RECEIPT ---")
print(f"School Name: {school_name}")
print(f"Tuition Fee:\t₦{tuition_fee:,.2f}")
print(f"Hostel Fee:\t₦{hostel_fee:,.2f}")
print(f"Feeding Fee:\t₦{feeding_fee:,.2f}")
print("---------------------------")
print(f"Total:\t\t₦{total_fee:,.2f}")
print("---------------------------")
