# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 1500,
    "MSFT": 300
}

def get_stock_input():
    stocks = {}
    while True:
        stock_name = input("Enter stock name (or type 'done' to finish): ").upper()
        if stock_name == 'DONE':
            break
        if stock_name not in stock_prices:
            print("Stock not recognized. Available stocks:", list(stock_prices.keys()))
            continue
        try:
            quantity = int(input(f"Enter quantity of {stock_name}: "))
            if quantity < 0:
                print("Quantity cannot be negative. Try again.")
                continue
            stocks[stock_name] = stocks.get(stock_name, 0) + quantity
        except ValueError:
            print("Invalid input for quantity. Please enter a number.")
    return stocks

def calculate_total_investment(stocks):
    total = 0
    for stock, quantity in stocks.items():
        total += stock_prices[stock] * quantity
    return total

def save_to_file(stocks, total, filename="portfolio.txt"):
    with open(filename, "w") as file:
        file.write("Stock Portfolio:\n")
        for stock, quantity in stocks.items():
            file.write(f"{stock}: {quantity} shares @ ${stock_prices[stock]} each\n")
        file.write(f"\nTotal Investment: ${total}\n")
    print(f"Portfolio saved to {filename}")

def main():
    print("Welcome to the Stock Portfolio Tracker!")
    stocks = get_stock_input()
    if not stocks:
        print("No stocks entered.")
        return
    total = calculate_total_investment(stocks)
    print("\nYour Portfolio:")
    for stock, quantity in stocks.items():
        print(f"{stock}: {quantity} shares @ ${stock_prices[stock]} each")
    print(f"\nTotal Investment: ${total}")

    save_option = input("Do you want to save this portfolio? (yes/no): ").lower()
    if save_option == 'yes':
        save_to_file(stocks, total)

if __name__ == "__main__":
    main()