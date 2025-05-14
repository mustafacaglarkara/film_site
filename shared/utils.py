from datetime import datetime


def format_datetime(value, fmt="%d.%m.%Y %H:%M"):
    return value.strftime(fmt) if isinstance(value, datetime) else value
