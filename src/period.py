from dataclasses import dataclass, field
import datetime


@dataclass
class Period:
    start: str
    end: str
    start_datetime: datetime.datetime = field(init=False)
    end_datetime: datetime.datetime = field(init=False)

    def __post_init__(self) -> None:
        self.start_datetime = self.str_to_datetime(self.start, '%Y%m%d')
        self.end_datetime = self.str_to_datetime(self.end, '%Y%m%d')

    def get_date_list(self) -> set:
        return set([ d for d in self.gen_dates(self.start_datetime, ((self.end_datetime - self.start_datetime).days + 1))])

    @staticmethod
    def gen_dates(b_date, days):
        day = datetime.timedelta(days=1)
        for i in range(days):
            yield b_date + day * i

    @staticmethod
    def str_to_datetime(input_date_str: str, date_format: str) -> datetime.datetime:
        return datetime.datetime.strptime(input_date_str, date_format)