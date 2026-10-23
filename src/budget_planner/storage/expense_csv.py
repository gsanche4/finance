

import csv
from datetime import date
from budget_planner.domain.expense import Expense


def parse_date(value):
    if not value:
        return None
    return date.fromisoformat(value)


def load_expenses(csv_path):
    with open(csv_path, mode='r', encoding='utf-8', newline='') as file:
        reader = csv.DictReader(file)
        expenses = []

        for row in reader:
            row["start_date"] = parse_date(row["start_date"])
            row["end_date"] = parse_date(row["end_date"])
            expense = Expense.from_dict(row)
            expenses.append(expense)

        return expenses
