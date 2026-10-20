

from datetime import date


def parse_date(value):
    if not value:
        return None
    return date.strptime(value, "%Y-%m-%d")
