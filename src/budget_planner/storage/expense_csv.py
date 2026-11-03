import csv
from datetime import date
from uuid import UUID
from budget_planner.domain.expense import Expense
from budget_planner.domain.money import Money
from budget_planner.domain.payment_frequency import PaymentFrequency

REQUIRED_COLUMNS = (
    "id",
    "start_date",
    "end_date",
    "frequency",
    "category",
    "merchant",
    "description",
    "amount",
)


class ExpenseCsvError(ValueError):
    """The expenses file is missing columns or has a row that is invalid."""


def _parse_optional_date(value: str) -> date | None:
    if not value:
        return None
    return date.fromisoformat(value)


def _text(row: dict, column: str) -> str:
    return (row[column] or "").strip()


def _required_text(value: str) -> str:
    if not value:
        raise ValueError("must not be blank")
    return value


def _required_date(value: str) -> date:
    return date.fromisoformat(value)


def _parse_frequency(value: str) -> PaymentFrequency:
    return PaymentFrequency(value.lower())


def _parse_field(column: str, parse, value):
    try:
        return parse(value)
    except ValueError as error:
        raise ValueError(f"{column}: {error}") from error


def parse_expense_row(row: dict) -> Expense:
    return Expense(
        id=_parse_field("id", UUID, _text(row, "id")),
        start_date=_parse_field("start_date", _required_date, _text(row, "start_date")),
        end_date=_parse_field("end_date", _parse_optional_date, _text(row, "end_date")),
        frequency=_parse_field("frequency", _parse_frequency, _text(row, "frequency")),
        category=_parse_field("category", _required_text, _text(row, "category")),
        merchant=_parse_field("merchant", _required_text, _text(row, "merchant")),
        description=_text(row, "description") or None,
        amount=_parse_field("amount", Money.from_str, _text(row, "amount")),
    )


def load_expenses(csv_path) -> list[Expense]:
    with open(csv_path, mode="r", encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)

        missing = [
            column
            for column in REQUIRED_COLUMNS
            if column not in (reader.fieldnames or [])
        ]
        if missing:
            raise ExpenseCsvError(
                f"{csv_path}: missing column(s): {', '.join(missing)}"
            )

        expenses = []
        seen_ids = set()

        # Line 1 is the header, so the first data row is line 2.
        for line_number, row in enumerate(reader, start=2):
            try:
                expense = parse_expense_row(row)
            except ValueError as error:
                raise ExpenseCsvError(
                    f"{csv_path} line {line_number}: {error}"
                ) from error

            if expense.id in seen_ids:
                raise ExpenseCsvError(
                    f"{csv_path} line {line_number}: " f"duplicate id {expense.id}"
                )
            seen_ids.add(expense.id)
            expenses.append(expense)

        return expenses
