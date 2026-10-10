from dataclasses import dataclass
from datetime import datetime


@dataclass
class Expense:
    start_date: datetime
    end_date: datetime | None
    category: str
    merchant: str
    description: str | None
    amount: str

    @classmethod
    def from_dict(cls, row: dict):
        return cls(
            start_date=row["start_date"],
            end_date=row["end_date"],
            category=row["category"],
            merchant=row["merchant"],
            description=row["description"],
            amount=float(row["amount"])
        )
