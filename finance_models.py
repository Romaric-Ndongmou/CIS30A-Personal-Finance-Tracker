# finance_models

class Budget:
    # Stores budget information
    
    def __init__(self, period, budget_limit, savings_goal):
        self.period = period
        self.budget_limit = budget_limit
        self.savings_goal = savings_goal

    #checks if user is within budget
        
    def budget_status(self, total_expenses):
        if total_expenses <= self.budget_limit:
            remaining = self.budget_limit - total_expenses
            return "WITHIN BUDGET (Remaining: $" + format(remaining, ".2f") + ")"
        else:
            over = total_expenses - self.budget_limit
            return "OVER BUDGET (Over by: $" + format(over, ".2f") + ")"

    #checks savings goal
        
    def savings_status(self, net_balance):
        if net_balance >= self.savings_goal:
            return "SAVINGS GOAL MET"
        else:
            need = self.savings_goal - net_balance
            return "SAVINGS GOAL NOT MET (Need: $" + format(need, ".2f") + ")"


class Transaction:
    # Base class for transactions
    def __init__(self, name, category, amount, date_text):
        self.name = name
        self.category = category
        self.amount = amount
        self.date_text = date_text

    #return a string line for displaying
        
    def show(self):
        return self.date_text + " | " + self.name + " | " + self.category + " | $" + format(self.amount, ".2f")

    # Method: type label
    def kind(self):
        return "Transaction"


class Income(Transaction):
    
    # Subclass of Transaction
    
    def kind(self):
        return "Income"


class Expense(Transaction):
    
    # Subclass of Transaction
    
    def kind(self):
        return "Expense"
