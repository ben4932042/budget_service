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


class BudgetService:

    def __init__(self):
        self.db_result = BudgetRepo.get_all()

    def query(self, start: str, end: str) -> float:
        start_datetime = self.str_to_datetime(start)
        end_datetime = self.str_to_datetime(end)
        if start_datetime > end_datetime: return float(0)
        month_list = sorted(self.get_date_list(start_datetime, end_datetime))
        if len(month_list) == 0: return float(0)
        if len(month_list) == 1:
            delta_days = (end_datetime - start_datetime ).days + 1
            full_month_days = self.get_month_have_days( start_datetime.year, start_datetime.month )
            return self.db_result.get( f"{start_datetime.year}{start_datetime.month}", 0) * (delta_days/full_month_days)

        else:
            start_month_days = self.last_day_of_month(start_datetime).day
            end_month_days = self.last_day_of_month(end_datetime).day
            start_month_percentage = (start_month_days - start_datetime.day + 1)/start_month_days
            end_month_percentage = (end_datetime.day) / end_month_days

            start_month_budget = self.db_result.get(month_list[0], 0)*start_month_percentage
            end_month_budget = self.db_result.get(month_list[-1], 0)*end_month_percentage
            interval_month_list = month_list[1: -1]
            interval_month_budget = 0
            if len(interval_month_list) > 0:
                for each_month in interval_month_list:
                    interval_month_budget += self.db_result.get(each_month, 0)
            return start_month_budget + end_month_budget + interval_month_budget


    def get_month_have_days(self, year, month) -> int:
        return calendar.monthrange( year, month )[1]

    def str_to_datetime(self, input_date_str: str) -> datetime.datetime:
        return datetime.datetime.strptime( input_date_str, "%Y%m%d" )

    def gen_dates(self, b_date, days):
        day = datetime.timedelta( days=1 )
        # print(day)
        for i in range( days ):
            # print(b_date + day*i)
            yield b_date + day * i

    def get_date_list(self, start_date, end_date):  # end_date=None

        data = []
        for d in self.gen_dates( start_date, ((end_date - start_date).days + 1) ):  # 29 + 1
            data.append( d.strftime( "%Y%m" ) )
        return list( set( data ) )

    def last_day_of_month(self, any_day: datetime.datetime) -> datetime.datetime:
        """
        :param any_day: any datetime
        :return: datetime.datetime
        """
        # this will never fail
        next_month = any_day.replace(day=28) + relativedelta(days=4)
        return next_month - relativedelta(days=next_month.day)