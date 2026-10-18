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


def sort_expenses_by_due_date(expenses: list[Expense]) -> list[Expense]:
    if not expenses:
        return []

    expenses.sort(
        key=lambda expense:
        PaymentScheduler().next_due_date(expense, datetime.now())
    )

    return expenses


def print_expenses(expenses: list[Expense]) -> None:
    if not expenses:
        print("No expenses found.")
        return

    expenses = sort_expenses_by_due_date(expenses)

    print(f"{'Merchant':<20} {'Category':<15} {'Amount':>12} {'Due Date':>12}")
    print("-" * 62)

    for expense in expenses:
        expense_date = (
            PaymentScheduler()
            .next_due_date(expense, datetime.now())
            .strftime("%m/%d/%y")
        )

        print(
            f"{expense.merchant:<20} "
            f"{expense.category:<15} "
            f"${expense.amount:>9,.2f} "
            f"{expense_date:>12}"
        )

    print("-" * 62)

    total = sum(expense.amount for expense in expenses)
    print(f"{'Total':<35} ${total:>11,.2f}")


def view_expenses():
    expenses = load_expenses('expenses.csv')
    print_expenses(expenses)


def print_payment_schedule():
    expenses = load_expenses('expenses.csv')
    payment_schedule = PaymentScheduler().payment_schedule_by_expense(
        expense=expenses[0],
        schedule_start_date=datetime(2026, 10, 1),
        schedule_end_date=datetime(2027, 1, 15)
    )

    print(expenses[0].merchant)
    print(payment_schedule)
