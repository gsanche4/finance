

from budget_planner.domain.expense_occurrence import ExpenseOccurrence


def expense_table(expense_occurrences: list[ExpenseOccurrence]) -> None:
    if not expense_occurrences:
        print("No expenses found.")
        return

    print(f"{'Merchant':<20} {'Category':<15} {'Amount':>12} {'Due Date':>12}")
    print("-" * 62)

    total_expense_amount = 0
    for occurrence in expense_occurrences:
        expense = occurrence.expense
        total_expense_amount += expense.amount
        print(
            f"{expense.merchant:<20} "
            f"{expense.category:<15} "
            f"${expense.amount:>9,.2f} "
            f"{occurrence.due_date.strftime('%m/%d/%y'):>12}"
        )

    print("-" * 62)
    print(f"{'Total':<35} ${total_expense_amount:>11,.2f}")
