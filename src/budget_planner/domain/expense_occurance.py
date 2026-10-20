

from dataclasses import dataclass

from domain.expense import Expense
from datetime import date


@dataclass
class ExpenseOccurance:
    expense: Expense
    due_date: date
