import datetime
import calendar
from dateutil.relativedelta import relativedelta


def str_to_datetime(input_date_str: str, format="%Y%m%d") -> datetime.datetime:
    return datetime.datetime.strptime(input_date_str, format)


def gen_dates(b_date, days):
    day = datetime.timedelta(days=1)
    for i in range(days):
        yield b_date + day * i


def get_date_list(start_date, end_date) -> set:  # end_date=None
    start_date, end_date = str_to_datetime( start_date ), str_to_datetime( end_date )
    return set([d for d in gen_dates(start_date, ((end_date - start_date).days + 1))])


def last_day_of_month(any_day: datetime.datetime) -> datetime.datetime:
    """
    :param any_day: any datetime
    :return: datetime.datetime
    """
    # this will never fail
    next_month = any_day.replace(day=28) + relativedelta(days=4)
    return next_month - relativedelta(days=next_month.day)


def get_month_have_days(year: int, month: int) -> int:
    """

    :rtype: object
    """
    return calendar.monthrange( year, month )[1]


def get_month_days(year_month: str) -> int:
    year_month_datetime = datetime.datetime.strptime( year_month, "%Y%m" )
    year = year_month_datetime.year
    month = year_month_datetime.month
    return get_month_have_days(year, month)