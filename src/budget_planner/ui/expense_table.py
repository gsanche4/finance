from budget_planner.domain.expense_occurrence import ExpenseOccurrence
from budget_planner.domain.money import Money

MERCHANT_WIDTH = 20
CATEGORY_WIDTH = 15
AMOUNT_WIDTH = 12
DATE_WIDTH = 12
TABLE_WIDTH = MERCHANT_WIDTH + CATEGORY_WIDTH + AMOUNT_WIDTH + DATE_WIDTH + 3


def _fit(text: str, width: int) -> str:
    if len(text) <= width:
        return text
    return text[: width - 1] + "…"


def _dollars(amount: Money) -> str:
    return f"${amount:,.2f}"


def expense_table(expense_occurrences: list[ExpenseOccurrence]) -> str:
    if not expense_occurrences:
        return "No expenses found."

    lines = [
        f"{'Merchant':<{MERCHANT_WIDTH}} {'Category':<{CATEGORY_WIDTH}} "
        f"{'Amount':>{AMOUNT_WIDTH}} {'Due Date':>{DATE_WIDTH}}",
        "-" * TABLE_WIDTH,
    ]

    for occurrence in expense_occurrences:
        expense = occurrence.expense
        due_date = occurrence.due_date.strftime("%m/%d/%y")
        lines.append(
            f"{_fit(expense.merchant, MERCHANT_WIDTH):<{MERCHANT_WIDTH}} "
            f"{_fit(expense.category, CATEGORY_WIDTH):<{CATEGORY_WIDTH}} "
            f"{_dollars(expense.amount):>{AMOUNT_WIDTH}} "
            f"{due_date:>{DATE_WIDTH}}"
        )

    total_amount = sum(
        (occurrence.expense.amount for occurrence in expense_occurrences), Money.zero()
    )
    label_width = MERCHANT_WIDTH + 1 + CATEGORY_WIDTH
    lines.append("-" * TABLE_WIDTH)
    lines.append(f"{'Total':<{label_width}} {_dollars(total_amount):>{AMOUNT_WIDTH}}")

    return "\n".join(lines)
