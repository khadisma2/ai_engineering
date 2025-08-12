# Step 1: Display a welcome screen
print("Welcome to KHADISMA Mobile Services!")
print("Good day! How can we help you today?\n")

# Step 2: Ask the user to dial a USSD code
ussd_code = input("Please dial your USSD code (e.g *123#): ")

# Step 3: Print menu options
print("\nUSSD Menu:")
print("1. Check Balance\n2. Buy Airtime\n3. Buy Data")

# Step 4: Ask the user to choose an option
choice = input("\nEnter your choice (1, 2, or 3): ")

# Step 5: Display confirmation of selected option
if choice == "1":
    print(f"\nYou selected: Check Balance")
    print("Your current balance is ₦5,000.00. Thank you for using KHADISMA Mobile Services!")
elif choice == "2":
    amount = float(input("\nEnter airtime amount (₦): "))
    print(f"\nYou selected: Buy Airtime")
    print(f"Processing your airtime purchase of ₦{amount:,.2f}...")
    print(f"Transaction successful! You have recharged ₦{amount:,.2f}.")
elif choice == "3":
    amount = float(input("\nEnter data amount in Naira (₦): "))
    print(f"\nYou selected: Buy Data")
    print(f"Processing your data purchase of ₦{amount:,.2f}...")
    print(f"Transaction successful! You have purchased data worth ₦{amount:,.2f}.")
else:
    print("\nInvalid option. Please try again.")
