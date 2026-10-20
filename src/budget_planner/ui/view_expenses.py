

from budget_planner.domain.sort_expenses_by_due_date import (
    sort_expenses_by_due_date
)
from budget_planner.storage.load_expenses import load_expenses
from budget_planner.ui.print_expenses import print_expenses


def view_expenses(data_path: str) -> None:
    expenses = load_expenses(data_path)
    expenses = sort_expenses_by_due_date(expenses)
    print_expenses(expenses)
