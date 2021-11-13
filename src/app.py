import dataclasses
import datetime
import calendar
from dateutil.relativedelta import relativedelta


@dataclasses.dataclass
class Budget:
    # data structure
    YearMonth: str
    Amount: int


class BudgetRepo:
    def get_all(self) -> dict:
        """get add data in db"""


def str_to_datetime(input_date_str: str) -> datetime.datetime:
    return datetime.datetime.strptime( input_date_str, "%Y%m%d" )


def gen_dates(b_date, days):
    day = datetime.timedelta( days=1 )
    # print(day)
    for i in range( days ):
        # print(b_date + day*i)
        yield b_date + day * i


def get_date_list(start_date, end_date) -> set:  # end_date=None
    return set( [d.strftime( "%Y%m" ) for d in gen_dates( start_date, ((end_date - start_date).days + 1) )] )


def last_day_of_month(any_day: datetime.datetime) -> datetime.datetime:
    """
    :param any_day: any datetime
    :return: datetime.datetime
    """
    # this will never fail
    next_month = any_day.replace( day=28 ) + relativedelta( days=4 )
    return next_month - relativedelta( days=next_month.day )


def get_month_have_days(year: int, month: int) -> int:
    return calendar.monthrange( year, month )[1]


class BudgetService:

    def __init__(self):
        self.db_result = BudgetRepo.get_all()

    def query(self, start: str, end: str) -> float:
        start_datetime = str_to_datetime( start )
        end_datetime = str_to_datetime( end )
        if start_datetime > end_datetime: return float( 0 )
        month_list = sorted( get_date_list( start_datetime, end_datetime ) )

        if len( month_list ) == 1:
            delta_days = (end_datetime - start_datetime).days + 1
            full_month_days = get_month_have_days( start_datetime.year, start_datetime.month )
            return_budget = self.db_result.get( f"{start_datetime.year}{start_datetime.month}", 0 ) * (
                        delta_days / full_month_days)

        else:
            start_month_days = last_day_of_month( start_datetime ).day
            end_month_days = last_day_of_month( end_datetime ).day
            start_month_percentage = (start_month_days - start_datetime.day + 1) / start_month_days
            end_month_percentage = end_datetime.day / end_month_days
            start_month_budget = self.db_result.get( month_list[0], 0 ) * start_month_percentage
            end_month_budget = self.db_result.get( month_list[-1], 0 ) * end_month_percentage

            interval_month_budget = sum([self.db_result.get( each_month, 0 ) for each_month in month_list[1: -1]])
            return_budget = start_month_budget + end_month_budget + interval_month_budget

        return return_budget

