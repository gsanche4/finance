

from budget_planner.domain.expense import Expense
from budget_planner.domain.schedule import first_occurrence_on_or_after
from datetime import date


def sort_expenses_by_due_date(expenses: list[Expense]) -> list[Expense]:
    if not expenses:
        return []

    expenses.sort(
        key=lambda expense:
        first_occurrence_on_or_after(expense, date.today()).due_date
    )

    return expenses
