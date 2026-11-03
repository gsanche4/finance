from budget_planner.domain.expense_occurrence import ExpenseOccurrence
from budget_planner.domain.expense import Expense
from budget_planner.domain.schedule import first_occurrence_on_or_after
from datetime import date


def next_occurrences(expenses: list[Expense], today: date) -> list[ExpenseOccurrence]:
    occurrences = []
    for expense in expenses:
        occurrence = first_occurrence_on_or_after(expense, today)
        if occurrence is not None:
            occurrences.append(occurrence)

    return sorted(occurrences, key=lambda o: o.due_date)
