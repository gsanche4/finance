

from budget_planner.domain.expense import Expense
from budget_planner.domain.payment_scheduler import PaymentScheduler
from datetime import datetime


def sort_expenses_by_due_date(expenses: list[Expense]) -> list[Expense]:
    if not expenses:
        return []

    expenses.sort(
        key=lambda expense:
        PaymentScheduler().next_due_date(expense, datetime.now())
    )

    return expenses
