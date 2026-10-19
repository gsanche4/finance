

from enum import Enum


class PaymentFrequency(Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    YEARLY = "yearly"
    UNKNOWN = "unknown"

    @classmethod
    def from_str(cls, value: str) -> "PaymentFrequency":
        try:
            normalized_value = value.strip().lower()
            return cls(normalized_value)
        except (ValueError, AttributeError):
            return cls.UNKNOWN
