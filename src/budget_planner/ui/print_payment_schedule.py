

from budget_planner.storage.load_expenses import load_expenses
from budget_planner.domain.payment_scheduler import PaymentScheduler
from datetime import datetime


FILEPATH = 'data/expenses.csv'


def print_payment_schedule():
    expenses = load_expenses(FILEPATH)
    payment_schedule = PaymentScheduler().payment_schedule_by_expense(
        expense=expenses[0],
        schedule_start_date=datetime(2026, 10, 1),
        schedule_end_date=datetime(2027, 1, 15)
    )

    print(expenses[0].merchant)
    print(payment_schedule)
