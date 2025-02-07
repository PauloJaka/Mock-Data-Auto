from .base_generator import BaseGenerator
import random


class BigintGenerator(BaseGenerator):
    def generate_data(self, column_type: str, nullable: bool = False) -> int:
        if nullable and random.random() < 0.1:
            return None
        return random.randint(1, 1000000)
