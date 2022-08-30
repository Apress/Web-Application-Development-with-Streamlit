from dataclasses import dataclass
import datetime


@dataclass(init=True)
class Post:
    creator_name: str
    content: str
    posting_date: datetime.datetime
