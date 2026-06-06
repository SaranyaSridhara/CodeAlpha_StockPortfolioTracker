stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 420
}

total_investment = 0
portfolio_details = []

n = int(input("Enter the number of stocks: "))

for i in range(n):
    stock_name = input("\nEnter stock name: ").upper()

    if stock_name in stock_prices:
        quantity = int(input("Enter quantity: "))

        investment = stock_prices[stock_name] * quantity
        total_investment += investment

        portfolio_details.append(
            f"{stock_name}, Quantity: {quantity}, Investment: ${investment}"
        )
    else:
        print("Stock not found!")

print("\n----- Portfolio Summary -----")
for item in portfolio_details:
    print(item)

print(f"\nTotal Investment Value: ${total_investment}")

# Save result to a text file
with open("portfolio.txt", "w") as file:
    file.write("Portfolio Summary\n")
    file.write("-----------------\n")

    for item in portfolio_details:
        file.write(item + "\n")

    file.write(f"\nTotal Investment Value: ${total_investment}")

print("\nPortfolio details saved to portfolio.txt")
