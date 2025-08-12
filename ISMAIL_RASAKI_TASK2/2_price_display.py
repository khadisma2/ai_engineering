# Ask the user for the price of garri per paint in naira (as a string)
price_str = input("Enter the price of garri per paint in naira: ")

# Convert to float
price = float(price_str)

# Display amount in naira and kobo
print(f"The price of garri per paint is ₦{price:.2f} (in naira and kobo).")


