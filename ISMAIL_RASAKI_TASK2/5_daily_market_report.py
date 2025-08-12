# Daily Market Report
market_name = input("Enter the market name: ")
number = int(input("Enter number of traders: "))
price_str = float(input("Enter daily revenue in naira: "))
print(f"Market name: {market_name}\nNumbers of traders: {number}\nDialy revenue: #{price_str:,.2f}")


# Ask for market name, number of traders, and daily revenue in naira
market_name = input("Enter the market name: ")
num_traders = int(input("Enter the number of traders: "))
daily_revenue = float(input("Enter the daily revenue in naira: "))
print(f"Market: {market_name}\nNumber of traders: {num_traders:,}\nDaily revenue: ₦{daily_revenue:,.2f}")
