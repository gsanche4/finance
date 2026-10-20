

from budget_planner.domain.expense import Expense
from budget_planner.domain.payment_scheduler import PaymentScheduler
from datetime import date


def print_expenses(expenses: list[Expense]) -> None:
    if not expenses:
        print("No expenses found.")
        return

    print(f"{'Merchant':<20} {'Category':<15} {'Amount':>12} {'Due Date':>12}")
    print("-" * 62)

    for expense in expenses:
        expense_date = (
            PaymentScheduler()
            .next_due_date(expense, date.today())
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
