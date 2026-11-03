from budget_planner.domain.next_occurrences import next_occurrences
from budget_planner.domain.expense import Expense
from budget_planner.ui.expense_table import expense_table
from datetime import date


def view_expenses(expenses: list[Expense], today: date) -> None:
    expense_occurrences = next_occurrences(expenses=expenses, today=today)
    print(expense_table(expense_occurrences))
