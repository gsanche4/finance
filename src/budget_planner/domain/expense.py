from dataclasses import dataclass, field
from datetime import date
from uuid import UUID, uuid4
from budget_planner.domain.money import Money
from budget_planner.domain.payment_frequency import PaymentFrequency


@dataclass(eq=False)
class Expense:
    start_date: date
    end_date: date | None
    frequency: PaymentFrequency
    category: str
    merchant: str
    description: str | None
    amount: Money
    id: UUID = field(default_factory=uuid4)

    def __post_init__(self):
        if self.end_date is not None and self.end_date < self.start_date:
            raise ValueError("end_date cannot be before start_date")

    def __eq__(self, other):
        if not isinstance(other, Expense):
            return NotImplemented
        return self.id == other.id

    def __hash__(self):
        return hash(self.id)
