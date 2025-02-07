import random

from .base_generator import BaseGenerator


class CPFGenerator(BaseGenerator):
    def generate_data(self, column_type: str, nullable: bool = False) -> str:
        if nullable and random.random() < 0.1:
            return None

        # Generate a valid CPF
        def calculate_cpf_check_digits(base_cpf):
            total1 = sum((10 - i) * int(digit) for i, digit in enumerate(base_cpf))
            remainder1 = total1 % 11
            check_digit1 = 0 if remainder1 < 2 else 11 - remainder1

            total2 = sum(
                (11 - i) * int(digit)
                for i, digit in enumerate(base_cpf + str(check_digit1))
            )
            remainder2 = total2 % 11
            check_digit2 = 0 if remainder2 < 2 else 11 - remainder2

            return str(check_digit1) + str(check_digit2)

        base_cpf = "".join(str(random.randint(0, 9)) for _ in range(9))
        check_digits = calculate_cpf_check_digits(base_cpf)

        return base_cpf + check_digits
