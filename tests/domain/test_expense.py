from dataclasses import replace
from datetime import date
import unittest
import uuid

from budget_planner.domain.expense import Expense
from budget_planner.domain.money import Money
from budget_planner.domain.payment_frequency import PaymentFrequency


def _create_expense(**kwargs) -> Expense:
    defaults = {
        "start_date": date(2024, 6, 1),
        "end_date": None,
        "frequency": PaymentFrequency.MONTHLY,
        "category": "Utility",
        "merchant": "ABC Company",
        "description": "Phone Bill",
        "amount": Money.from_str("20.99"),
    }
    defaults.update(kwargs)
    return Expense(**defaults)


class TestInitialization(unittest.TestCase):
    def test_end_date_before_start_date_is_rejected(self):
        with self.assertRaises(ValueError):
            _create_expense(start_date=date(2001, 1, 1), end_date=date(2000, 1, 1))

    def test_end_date_on_start_date_is_allowed(self):
        _create_expense(start_date=date(2000, 1, 1), end_date=date(2000, 1, 1))

    def test_none_end_date_is_allowed(self):
        _create_expense(end_date=None)


class TestEquality(unittest.TestCase):
    def setUp(self):
        self.expense = _create_expense()

    def test_same_id_is_equal_even_if_fields_differ(self):
        other_expense = replace(self.expense, amount=Money.from_str("10.72"))

        self.assertEqual(self.expense, other_expense)

    def test_different_id_not_equal_even_if_fields_are_the_same(self):
        other_expense = replace(self.expense, id=uuid.uuid4())

        self.assertNotEqual(self.expense, other_expense)

    def test_type_mismatch_returns_false(self):
        self.assertNotEqual(self.expense, "Not an expense object")


class TestHashing(unittest.TestCase):
    def test_expenses_with_same_id_count_as_one_item_in_set(self):
        expense = _create_expense()
        other_expense = replace(expense, amount=Money.from_str("20.42"))
        expense_set = {expense, other_expense}

        self.assertEqual(len(expense_set), 1)
