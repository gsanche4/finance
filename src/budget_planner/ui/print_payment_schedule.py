

from budget_planner.storage.load_expenses import load_expenses
from budget_planner.domain.schedule import occurrences_between
from datetime import date


FILEPATH = 'data/expenses.csv'


def print_payment_schedule():
    expenses = load_expenses(FILEPATH)
    payment_schedule = occurrences_between(
        expense=expenses[0],
        start=date(2026, 10, 1),
        end=date(2027, 1, 15)
    )

    print(expenses[0].merchant)
    print(payment_schedule)
