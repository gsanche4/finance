from dataclasses import dataclass
from decimal import Decimal, InvalidOperation

_CENT = Decimal("0.01")


@dataclass(frozen=True, order=True)
class Money:
    """An exact dollar amount, always held to two decimal places."""

    amount: Decimal

    def __post_init__(self):
        if not isinstance(self.amount, Decimal):
            raise TypeError("Money needs a Decimal amount; use Money.from_str('5.99')")
        if not self.amount.is_finite():
            raise ValueError(f"Money must be a finite number, got {self.amount}")

        rounded = self.amount.quantize(_CENT)
        if rounded != self.amount:
            raise ValueError(
                f"Money allows at most 2 decimal places, got {self.amount}"
            )
        object.__setattr__(self, "amount", rounded)

    @classmethod
    def from_str(cls, text: str) -> "Money":
        try:
            return cls(Decimal(text.strip()))
        except InvalidOperation:
            raise ValueError(f"not a valid money amount: {text!r}") from None

    @classmethod
    def zero(cls) -> "Money":
        return cls(Decimal("0.00"))

    def __add__(self, other):
        if not isinstance(other, Money):
            return NotImplemented
        return Money(self.amount + other.amount)

    def __format__(self, spec: str) -> str:
        return format(self.amount, spec)

    def __str__(self) -> str:
        return f"{self.amount:,.2f}"
