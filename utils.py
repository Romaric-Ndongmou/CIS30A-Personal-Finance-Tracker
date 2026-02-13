def get_text(prompt):
    
    # Keep asking until user enters text
    while True:
        text = input(prompt).strip()
        if text != "":
            return text
        print("Error: This field cannot be empty.")


def get_positive_number(prompt):
    
    # Keep asking until user enters a valid positive number
    while True:
        try:
            value = float(input(prompt))
            if value > 0:
                return value
            else:
                print("Error: Number must be greater than 0.")
        except ValueError:
            print("Error: Please enter a valid number (example: 25.50).")


def compute_totals(transactions, IncomeClass, ExpenseClass):
    
    # Computation of the totals
    total_income = 0
    total_expenses = 0

    for t in transactions:  # loop requirement
        if isinstance(t, IncomeClass):
            total_income = total_income + t.amount
        elif isinstance(t, ExpenseClass):
            total_expenses = total_expenses + t.amount

    net = total_income - total_expenses
    return total_income, total_expenses, net


def save_summary_txt(filename, budget, transactions, IncomeClass, ExpenseClass):
    
    # Save everything to a TXT file 
    total_income, total_expenses, net = compute_totals(transactions, IncomeClass, ExpenseClass)

    f = open(filename, "w")

    # Using print to write to file 
    print("PERSONAL FINANCE TRACKER SUMMARY", file=f)
    print("                                ", file=f)
    print("Period:", budget.period, file=f)
    print("Budget Limit: $", format(budget.budget_limit, ".2f"), file=f)
    print("Savings Goal: $", format(budget.savings_goal, ".2f"), file=f)
    print("", file=f)

    print("Total Income: $", format(total_income, ".2f"), file=f)
    print("Total Expenses: $", format(total_expenses, ".2f"), file=f)
    print("Net Balance: $", format(net, ".2f"), file=f)
    print("", file=f)

    print("Status:", file=f)
    print(budget.budget_status(total_expenses), file=f)
    print(budget.savings_status(net), file=f)
    print("", file=f)

    print("Transactions:", file=f)
    if len(transactions) == 0:
        print("(No transactions)", file=f)
    else:
        for i in range(len(transactions)):
            t = transactions[i]
            print(str(i + 1) + ". " + t.kind() + " - " + t.show(), file=f)

    f.close()
