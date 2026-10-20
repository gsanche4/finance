

from budget_planner.domain.expense import Expense
from budget_planner.domain.payment_frequency import PaymentFrequency
from datetime import date
from dateutil.relativedelta import relativedelta


class PaymentScheduler:

    def next_due_date(self, expense: Expense, evaluation_date=None):
        if not evaluation_date:
            evaluation_date = expense.start_date

        if expense.end_date and expense.start_date > expense.end_date:
            return None

        current_due_date = expense.start_date

        if expense.frequency == PaymentFrequency.MONTHLY:

            months_elapsed = 1
            while current_due_date < evaluation_date:
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
        schedule_start_date: date,
        schedule_end_date: date
    ):
        if schedule_end_date < expense.start_date:
            return []
        if expense.end_date and schedule_start_date > expense.end_date:
            return []

        payments = []

        search_start = max(expense.start_date, schedule_start_date)
        current_payment = self.next_due_date(
            expense=expense,
            evaluation_date=search_start
        )

        while current_payment and current_payment <= schedule_end_date:
            if expense.end_date and current_payment > expense.end_date:
                break

            payments.append(current_payment)

            current_payment = self.next_due_date(
                expense=expense,
                evaluation_date=(current_payment + relativedelta(days=1))
            )

        return payments
