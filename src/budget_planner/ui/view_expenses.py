

from budget_planner.storage.load_expenses import load_expenses
from budget_planner.ui.print_expenses import print_expenses


FILEPATH = 'data/expenses.csv'


def view_expenses():
    expenses = load_expenses(FILEPATH)
    print_expenses(expenses)
