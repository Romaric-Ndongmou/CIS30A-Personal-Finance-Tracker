from finance_models import Budget, Income, Expense
import utils


def show_menu():
    print("MENU")
    print("1) Add Income")
    print("2) Add Expense")
    print("3) View Summary")
    print("4) Update Transaction")
    print("5) Delete Transaction")
    print("6) Save Summary to Text File")
    print("0) Exit")


def list_transactions(transactions):
    if len(transactions) == 0:
        print("\nNo transactions recorded.\n")
        return

    print("\nTRANSACTIONS")
    print("ID | Type   | Date | Name | Category | Amount")
    print("                                             ")
    for i in range(len(transactions)):  # loop requirement
        t = transactions[i]
        print(str(i + 1) + " | " + t.kind() + " | " + t.show())
    print()


def add_income(transactions):
    print("\nAdd Income")
    name = utils.get_text("Name: ")
    category = utils.get_text("Category: ")
    amount = utils.get_positive_number("Amount: $")
    date_text = utils.get_text("Date (example 2026-02-12): ")

    transactions.append(Income(name, category, amount, date_text))
    print("Income added.\n")


def add_expense(transactions):
    print("\nAdd Expense")
    name = utils.get_text("Name: ")
    category = utils.get_text("Category: ")
    amount = utils.get_positive_number("Amount: $")
    date_text = utils.get_text("Date (example 2026-02-12): ")

    transactions.append(Expense(name, category, amount, date_text))
    print("Expense added.\n")


def view_summary(budget, transactions):
    total_income, total_expenses, net = utils.compute_totals(transactions, Income, Expense)

    print("\nSUMMARY")
    print("Total Income: $", format(total_income, ".2f"))
    print("Total Expenses: $", format(total_expenses, ".2f"))
    print("Net Balance: $", format(net, ".2f"))
    print("Budget Status:", budget.budget_status(total_expenses))
    print("Savings Status:", budget.savings_status(net))
    print()


def update_transaction(transactions):
    list_transactions(transactions)
    if len(transactions) == 0:
        return

    # exception handling requirement
    try:
        tx_id = int(input("Enter ID to update: "))
        if tx_id < 1 or tx_id > len(transactions):
            print("Error: ID not found.\n")
            return
    except ValueError:
        print("Error: Please enter a whole number.\n")
        return

    t = transactions[tx_id - 1]
    print("Leave blank to keep the same value.")

    new_name = input("New name (" + t.name + "): ").strip()
    new_cat = input("New category (" + t.category + "): ").strip()
    new_amt = input("New amount (" + str(t.amount) + "): ").strip()
    new_date = input("New date (" + t.date_text + "): ").strip()

    if new_name != "":
        t.name = new_name
    if new_cat != "":
        t.category = new_cat
    if new_date != "":
        t.date_text = new_date

    if new_amt != "":
        try:
            amt = float(new_amt)
            if amt > 0:
                t.amount = amt
            else:
                print("Error: amount must be > 0 (kept old amount).")
        except ValueError:
            print("Error: invalid amount (kept old amount).")

    print("Transaction updated.\n")


def delete_transaction(transactions):
    list_transactions(transactions)
    if len(transactions) == 0:
        return

    try:
        tx_id = int(input("Enter ID to delete: "))
        if tx_id < 1 or tx_id > len(transactions):
            print("Error: ID not found.\n")
            return
    except ValueError:
        print("Error: Please enter a whole number.\n")
        return

    removed = transactions.pop(tx_id - 1)
    print("Deleted:", removed.kind(), "-", removed.name, "\n")


def main():
    print("Welcome to the Personal Finance Tracker!\n")

    period = input("Choose period (weekly/monthly): ").strip().lower()
    if period != "weekly" and period != "monthly":
        period = "monthly"
        print("Invalid period entered. Defaulting to monthly.\n")

    budget_limit = utils.get_positive_number("Enter budget limit: $")
    savings_goal = utils.get_positive_number("Enter savings goal: $")

    budget = Budget(period, budget_limit, savings_goal)
    transactions = []  # list requirement

    while True:  # loop requirement
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_income(transactions)
        elif choice == "2":
            add_expense(transactions)
        elif choice == "3":
            list_transactions(transactions)
            view_summary(budget, transactions)
        elif choice == "4":
            update_transaction(transactions)
        elif choice == "5":
            delete_transaction(transactions)
        elif choice == "6":
            utils.save_summary_txt("finance_summary.txt", budget, transactions, Income, Expense)
            print("Saved to finance_summary.txt\n")
        elif choice == "0":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Try again.\n")


main()
