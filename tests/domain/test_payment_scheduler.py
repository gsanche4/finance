import unittest
from budget_planner.domain.payment_scheduler import PaymentScheduler
from budget_planner.domain.payment_frequency import PaymentFrequency
from budget_planner.domain.expense import Expense
from datetime import datetime


class TestPaymentScheduler(unittest.TestCase):

    def setUp(self):
        self.payment_scheduler = PaymentScheduler()
        self.expense = Expense(
            start_date=datetime(2026, 10, 6),
            end_date=datetime(2027, 10, 15),
            frequency=PaymentFrequency.MONTHLY,
            category="subscription",
            merchant="ABC Company",
            description=None,
            amount="5.99"
        )

    def test_next_due_date_adds_one_month(self):
        self.assertEqual(
            self.payment_scheduler.next_due_date(
                expense=self.expense,
                evaluation_date=datetime(2026, 10, 7)
            ),
            datetime(2026, 11, 6)
        )

    def test_next_due_date_handles_end_of_month(self):
        self.expense.start_date = datetime(2026, 1, 31)

        # Short month last day
        self.assertEqual(
            self.payment_scheduler.next_due_date(
                expense=self.expense,
                evaluation_date=datetime(2026, 2, 1)
            ),
            datetime(2026, 2, 28)
        )

        # After a short month, its still the last day
        self.assertEqual(
            self.payment_scheduler.next_due_date(
                expense=self.expense,
                evaluation_date=datetime(2026, 3, 1)
            ),
            datetime(2026, 3, 31)
        )

    def test_next_due_date_returns_none_if_end_date_reached(self):
        self.assertEqual(
            self.payment_scheduler.next_due_date(
                expense=self.expense,
                evaluation_date=datetime(2027, 10, 9)
            ),
            None
        )

    def test_next_due_date_returns_none_if_start_date_beyond_end_date(self):
        self.expense.start_date = datetime(2027, 10, 16)
        self.assertEqual(
            self.payment_scheduler.next_due_date(
                expense=self.expense
            ),
            None
        )
