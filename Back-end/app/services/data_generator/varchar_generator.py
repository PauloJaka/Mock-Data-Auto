import random

from .base_generator import BaseGenerator


class VarcharGenerator(BaseGenerator):
    def generate_data(
        self, column_type: str, nullable: bool = False, max_length: int = 255
    ) -> str:
        if nullable and random.random() < 0.1:
            return None

        if "name" or "nome" in column_type.lower():
            return self.fake.name()
        elif "email" or "mail" in column_type.lower():
            return self.fake.email()
        elif "password" or "senha" in column_type.lower():
            return self.fake.password()
        else:
            return self.fake.text(max_nb_chars=max_length)
