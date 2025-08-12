# Naira and exchange rates
amount_naira = float(input("Enter the amount in Naira: "))
rate_usd = float(input("Enter exchange rate to US Dollars: "))
rate_gbp = float(input("Enter exchange rate to British Pounds: "))

# Convert amounts
amount_usd = amount_naira / rate_usd
amount_gbp = amount_naira / rate_gbp

# Print results in table format
print("\n--- CURRENCY CONVERSION ---")
print(f"{'Currency':<15}{'Amount':>20}")
print("-" * 35)
print(f"{'Naira (₦)':<15}{'₦' + format(amount_naira, ',.2f'):>20}")
print(f"{'US Dollars ($)':<15}{'$' + format(amount_usd, ',.2f'):>20}")
print(f"{'British Pounds (£)':<15}{'£' + format(amount_gbp, ',.2f'):>20}")
print("-" * 35)
