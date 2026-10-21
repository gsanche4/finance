

from budget_planner.domain.expense_occurrence import ExpenseOccurrence
from budget_planner.domain.expense import Expense
from budget_planner.domain.schedule import first_occurrence_on_or_after
from datetime import date


def upcoming_occurrences(
        expenses: list[Expense],
        today: date
) -> list[ExpenseOccurrence]:

    if not expenses:
        return []

    occurrences = [
        first_occurrence_on_or_after(expense, today)
        for expense in expenses
    ]

    occurrences.sort(
        key=lambda occurrence:
        occurrence.due_date
    )

    return occurrences
