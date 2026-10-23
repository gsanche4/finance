

from enum import Enum


class PaymentFrequency(Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    YEARLY = "yearly"

    @classmethod
    def from_str(cls, value: str) -> "PaymentFrequency":
        normalized_value = value.strip().lower()
        return cls(normalized_value)
