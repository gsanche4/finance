import csv
from datetime import datetime
from dateutil.relativedelta import relativedelta
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


def payment_schedule(
    bill: Expense,
    schedule_start_date: datetime,
    schedule_end_date: datetime
):
    """
    start and end date are inclusive
    """

    if schedule_end_date < bill.start_date:
        return None

    if bill.end_date and schedule_start_date > bill.end_date:
        return None

    scheduled_dates = []
    current_bill_date = bill.start_date
    months_elapsed = 0

    while current_bill_date <= schedule_end_date:
        if bill.end_date and current_bill_date > bill.end_date:
            break

        if current_bill_date >= schedule_start_date:
            scheduled_dates.append(current_bill_date)
        months_elapsed += 1
        current_bill_date = (
            bill.start_date + relativedelta(months=months_elapsed)
        )

    return scheduled_dates


def start_up_app():
    expenses = load_expenses('expenses.csv')
    payment_schedule = PaymentScheduler().payment_schedule_by_expense(
        expense=expenses[0],
        schedule_start_date=datetime(2026, 10, 1),
        schedule_end_date=datetime(2027, 1, 15)
    )

    print(expenses[0].merchant)
    print(payment_schedule)


start_up_app()
