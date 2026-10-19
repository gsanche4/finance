

from datetime import datetime


def parse_date(value):
    if not value:
        return None
    return datetime.strptime(value, "%Y-%m-%d")
