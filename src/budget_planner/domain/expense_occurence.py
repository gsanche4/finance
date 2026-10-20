

from dataclasses import dataclass

from budget_planner.domain.expense import Expense
from datetime import date


@dataclass(frozen=True)
class ExpenseOccurence:
    expense: Expense
    due_date: date
