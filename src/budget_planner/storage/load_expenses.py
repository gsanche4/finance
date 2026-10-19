

import csv

from budget_planner.domain.expense import Expense
from budget_planner.storage.parse_date import parse_date


def load_expenses(file_path):
    with open(file_path, mode='r', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file)
        expenses = []

        for row in reader:
            row["start_date"] = parse_date(row["start_date"])
            row["end_date"] = parse_date(row["end_date"])
            expense = Expense.from_dict(row)
            expenses.append(expense)

        return expenses
