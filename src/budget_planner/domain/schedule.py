

from budget_planner.domain.expense import Expense
from budget_planner.domain.payment_frequency import PaymentFrequency
from budget_planner.domain.expense_occurence import ExpenseOccurence
from datetime import date
from dateutil.relativedelta import relativedelta


def first_occurrence_on_or_after(
        expense: Expense,
        day: date
) -> ExpenseOccurence | None:
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

    return ExpenseOccurence(expense=expense, due_date=current_due_date)


class PaymentScheduler:

    def next_due_date(self, expense: Expense, on_or_after=None):
        if not on_or_after:
            on_or_after = expense.start_date

        if expense.end_date and expense.start_date > expense.end_date:
            return None

        current_due_date = expense.start_date

        if expense.frequency == PaymentFrequency.MONTHLY:

            months_elapsed = 1
            while current_due_date < on_or_after:
                current_due_date = (
                    expense.start_date + relativedelta(months=months_elapsed)
                )
                months_elapsed += 1

        if expense.end_date and current_due_date > expense.end_date:
            return None

        return current_due_date

    def payment_schedule_by_expense(
        self,
        expense: Expense,
        range_start: date,
        range_end: date
    ):
        if range_end < expense.start_date:
            return []
        if expense.end_date and range_start > expense.end_date:
            return []

        payments = []

        search_start = max(expense.start_date, range_start)
        current_payment = self.next_due_date(
            expense=expense,
            on_or_after=search_start
        )

        while current_payment and current_payment <= range_end:
            if expense.end_date and current_payment > expense.end_date:
                break

            payments.append(current_payment)

            current_payment = self.next_due_date(
                expense=expense,
                on_or_after=(current_payment + relativedelta(days=1))
            )

        return payments
