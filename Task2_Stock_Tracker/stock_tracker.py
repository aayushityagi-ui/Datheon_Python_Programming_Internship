
# Stock Portfolio Performance Tracker

portfolio = []


def add_stock():
    print("\n--- Add Stock ---")

    name = input("Enter stock name: ").strip()

    if not name:
        print("Stock name cannot be empty.")
        return

    try:
        quantity = int(input("Enter quantity of shares: "))
        purchase_price = float(input("Enter purchase price per share: "))
        current_price = float(input("Enter current price per share: "))

        if quantity <= 0 or purchase_price <= 0 or current_price <= 0:
            print("Quantity and prices must be greater than zero.")
            return

        stock = {
            "name": name,
            "quantity": quantity,
            "purchase_price": purchase_price,
            "current_price": current_price
        }

        portfolio.append(stock)
        print(f"{name} added successfully!")

    except ValueError:
        print("Invalid input! Please enter valid numbers.")


def view_portfolio():
    print("\n--- Your Stock Portfolio ---")

    if not portfolio:
        print("Your portfolio is empty.")
        return

    print("-" * 75)
    print(f"{'Stock':<15}{'Quantity':<10}{'Purchase':<15}{'Current':<15}{'Profit/Loss':<15}")
    print("-" * 75)

    for stock in portfolio:
        investment = stock["quantity"] * stock["purchase_price"]
        current_value = stock["quantity"] * stock["current_price"]
        profit_loss = current_value - investment

        print(
            f"{stock['name']:<15}"
            f"{stock['quantity']:<10}"
            f"{stock['purchase_price']:<15.2f}"
            f"{stock['current_price']:<15.2f}"
            f"{profit_loss:<15.2f}"
        )

    print("-" * 75)


def calculate_performance():
    print("\n--- Portfolio Performance ---")

    if not portfolio:
        print("Your portfolio is empty.")
        return

    total_investment = 0
    total_current_value = 0

    for stock in portfolio:
        investment = stock["quantity"] * stock["purchase_price"]
        current_value = stock["quantity"] * stock["current_price"]

        total_investment += investment
        total_current_value += current_value

    profit_loss = total_current_value - total_investment

    if total_investment > 0:
        percentage = (profit_loss / total_investment) * 100
    else:
        percentage = 0

    print(f"Total Investment: ₹{total_investment:.2f}")
    print(f"Current Portfolio Value: ₹{total_current_value:.2f}")
    print(f"Total Profit/Loss: ₹{profit_loss:.2f}")
    print(f"Return Percentage: {percentage:.2f}%")

    if profit_loss > 0:
        print("Your portfolio is in profit!")
    elif profit_loss < 0:
        print("Your portfolio is in loss.")
    else:
        print("Your portfolio is at break-even.")


def remove_stock():
    print("\n--- Remove Stock ---")

    if not portfolio:
        print("Your portfolio is empty.")
        return

    for index, stock in enumerate(portfolio, start=1):
        print(f"{index}. {stock['name']}")

    try:
        choice = int(input("Enter stock number to remove: "))

        if 1 <= choice <= len(portfolio):
            removed_stock = portfolio.pop(choice - 1)
            print(f"{removed_stock['name']} removed successfully!")
        else:
            print("Invalid stock number.")

    except ValueError:
        print("Please enter a valid number.")


def main():
    while True:
        print("\n===== STOCK PORTFOLIO TRACKER =====")
        print("1. Add Stock")
        print("2. View Portfolio")
        print("3. Calculate Performance")
        print("4. Remove Stock")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_stock()

        elif choice == "2":
            view_portfolio()

        elif choice == "3":
            calculate_performance()

        elif choice == "4":
            remove_stock()

        elif choice == "5":
            print("Thank you for using Stock Portfolio Tracker!")
            break

        else:
            print("Invalid choice! Please select 1-5.")


# Run the program
if __name__ == "__main__":
    main()
