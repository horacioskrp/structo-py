import datetime


def utcnow() -> datetime:
    """
    Returns the current time in UTC but with tzinfo set
    """
    return datetime.datetime.now(datetime.timezone.utc)
