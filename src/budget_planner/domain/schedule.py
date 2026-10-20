

from budget_planner.domain.expense import Expense
from budget_planner.domain.payment_frequency import PaymentFrequency
from budget_planner.domain.expense_occurrence import ExpenseOccurrence
from datetime import date
from dateutil.relativedelta import relativedelta


def first_occurrence_on_or_after(
        expense: Expense,
        day: date
) -> ExpenseOccurrence:
    if not day:
        day = expense.start_date

    if expense.end_date and expense.start_date > expense.end_date:
        return None

    current_due_date = expense.start_date

    if expense.frequency == PaymentFrequency.MONTHLY:
        months_elapsed = 1
        while current_due_date < day:
            current_due_date = (
                expense.start_date + relativedelta(months=months_elapsed)
            )
            months_elapsed += 1

    if expense.end_date and current_due_date > expense.end_date:
        return None

    return ExpenseOccurrence(expense=expense, due_date=current_due_date)


def occurrences_between(
    expense: Expense,
    start: date,
    end: date
) -> list[ExpenseOccurrence]:
    if end < expense.start_date:
        return []
    if expense.end_date and start > expense.end_date:
        return []

    payments = []

    search_start = max(expense.start_date, start)
    current_payment = first_occurrence_on_or_after(
        expense=expense,
        day=search_start
    )

    while current_payment and current_payment.due_date <= end:
        if expense.end_date and current_payment.due_date > expense.end_date:
            break

        payments.append(current_payment)

        current_payment = first_occurrence_on_or_after(
            expense=expense,
            day=(current_payment.due_date + relativedelta(days=1))
        )

    return payments
