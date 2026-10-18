import csv
from datetime import datetime
from models.expense import Expense
from models.payment_scheduler import PaymentScheduler


def parse_date(value):
    if not value:
        return None
    return datetime.strptime(value, "%Y-%m-%d")


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


def print_payment_schedule():
    expenses = load_expenses('expenses.csv')
    payment_schedule = PaymentScheduler().payment_schedule_by_expense(
        expense=expenses[0],
        schedule_start_date=datetime(2026, 10, 1),
        schedule_end_date=datetime(2027, 1, 15)
    )

    print(expenses[0].merchant)
    print(payment_schedule)
