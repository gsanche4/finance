

from budget_planner.domain.upcoming_occurrences import (
    upcoming_occurrences
)
from budget_planner.domain.expense import Expense
from budget_planner.ui.expense_table import expense_table
from datetime import date


def view_expenses(expenses: list[Expense], day: date) -> None:
    expense_occurrences = upcoming_occurrences(expenses=expenses, today=day)
    expense_table(expense_occurrences)
