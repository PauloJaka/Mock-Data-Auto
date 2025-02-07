import random

from .base_generator import BaseGenerator


class BooleanGenerator(BaseGenerator):
    def generate_data(self, column_type: str, nullable: bool = False) -> bool:
        if nullable and random.random() < 0.1:
            return None
        return random.choice([True, False])
