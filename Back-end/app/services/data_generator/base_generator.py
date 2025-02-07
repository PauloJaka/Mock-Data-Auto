from typing import Any

from faker import Faker


class BaseGenerator:
    def __init__(self):
        self.fake = Faker("pt_BR")

    def generate_data(self, column_type: str, nullable: bool = False) -> Any:
        """
        Generate fake data based on column type

        Args:
            column_type (str): Type of column to generate
            nullable (bool): Whether the column can be null

        Returns:
            Generated fake data or None if nullable
        """
        raise NotImplementedError("Subclasses must implement this method")
