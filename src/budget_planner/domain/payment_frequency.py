from enum import Enum
from dateutil.relativedelta import relativedelta


class PaymentFrequency(Enum):
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    YEARLY = "yearly"

    @property
    def step(self) -> relativedelta:
        return _STEPS[self]


_STEPS = {
    PaymentFrequency.DAILY: relativedelta(days=1),
    PaymentFrequency.WEEKLY: relativedelta(weeks=1),
    PaymentFrequency.MONTHLY: relativedelta(months=1),
    PaymentFrequency.YEARLY: relativedelta(years=1),
}
