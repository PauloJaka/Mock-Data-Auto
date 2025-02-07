import random
from datetime import datetime

from .base_generator import BaseGenerator


class TimestampGenerator(BaseGenerator):
    def generate_data(self, column_type: str, nullable: bool = False) -> datetime:
        if nullable and random.random() < 0.1:
            return None
        return self.fake.date_time_this_decade()
