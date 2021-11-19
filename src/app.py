from typing import List

from src.budget import Budget
from src.period import Period
from src.utils import get_month_days


class BudgetRepo:
    def get_all(self) -> List[Budget]:
        """get add data in db
        :rtype: object
        """


class BudgetService:
    # TODO: Ben
    def __init__(self):
        self.db_result = BudgetRepo.get_all()

    def get_daily_amount(self, year_month) -> float:
        return self.db_result.get( year_month, 0 ) / get_month_days( year_month )

    def query(self, start: str, end: str) -> float:
        period = Period( start, end )

        return sum( [
            self.get_daily_amount( each_time.strftime( "%Y%m" ) )
            for each_time in period.get_date_list()
        ] )
