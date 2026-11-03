from budget_planner.domain.expense import Expense
from budget_planner.domain.expense_occurrence import ExpenseOccurrence
from datetime import date
from dateutil.relativedelta import relativedelta


def first_occurrence_on_or_after(
    expense: Expense, day: date
) -> ExpenseOccurrence | None:
    """First occurrence on or after `day`, or None if the expense has ended.

    Every date is computed from start_date (start + n * step), never from
    the previous date.
    """
    step = expense.frequency.step
    due_date = expense.start_date
    occurrence_number = 0

    while due_date < day:
        occurrence_number += 1
        due_date = expense.start_date + step * occurrence_number

    if expense.end_date and due_date > expense.end_date:
        return None

    return ExpenseOccurrence(expense=expense, due_date=due_date)


def occurrences_between(
    expense: Expense, first_day: date, last_day: date
) -> list[ExpenseOccurrence]:
    """All occurrences from `first_day` to `last_day`, both inclusive."""
    if last_day < expense.start_date:
        return []
    if expense.end_date and first_day > expense.end_date:
        return []

    occurrences = []

    search_start = max(expense.start_date, first_day)
    occurrence = first_occurrence_on_or_after(expense=expense, day=search_start)

    while occurrence and occurrence.due_date <= last_day:
        if expense.end_date and occurrence.due_date > expense.end_date:
            break

        occurrences.append(occurrence)

        occurrence = first_occurrence_on_or_after(
            expense=expense, day=(occurrence.due_date + relativedelta(days=1))
        )

    return occurrences
