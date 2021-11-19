from dataclasses import dataclass, field
import datetime
from typing import Dict

from src.utils import get_month_have_days


@dataclass
class Budget:
    # data structure
    YearMonth: str
    Amount: int
    year: int = field(init=False)
    month: int = field(init=False)

    def __post_init__(self) -> None:
        year_month_datetime = datetime.datetime.strptime(self.YearMonth, "%Y%m")
        self.year = year_month_datetime.year
        self.month = year_month_datetime.month

    def daily_amount(self):
        return self.Amount / get_month_have_days(self.year, self.month)

# @dataclass
# class BudgetList:
#     # data structure
#     YearMonth: str
#     Amount: int
#     year: int = field(init=False)
#     month: int = field(init=False)
#
#     def __post_init__(self) -> None:
#         year_month_datetime = datetime.datetime.strptime(self.YearMonth, "%Y%m")
#         self.year = year_month_datetime.year
#         self.month = year_month_datetime.month
#
#     def daily_amount(self):
#         return self.Amount / get_month_have_days(self.year, self.month)