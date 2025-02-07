from typing import Any, Dict, List

from .data_generator.bigint_generator import BigintGenerator
from .data_generator.boolean_generator import BooleanGenerator
from .data_generator.cpf_generator import CPFGenerator
from .data_generator.timestamp_generator import TimestampGenerator
from .data_generator.varchar_generator import VarcharGenerator


class DataGenerator:
    def __init__(self):
        self.generators = {
            "bigint": BigintGenerator(),
            "character varying": VarcharGenerator(),
            "timestamp with time zone": TimestampGenerator(),
            "boolean": BooleanGenerator(),
            "cpf": CPFGenerator(),
        }

    def generate_record(
        self, table_schema: Dict[str, Dict[str, str]]
    ) -> Dict[str, Any]:
        """
        Generate a single record based on table schema

        Args:
            table_schema (Dict): Dictionary of column definitions

        Returns:
            Generated record
        """
        record = {}
        for column, details in table_schema.items():
            column_type = details["type"]
            nullable = details.get("nullable", False)

            # Special handling for CPF
            if column == "cpf":
                generator = self.generators["cpf"]
            else:
                generator = self.generators.get(column_type)

            if generator:
                record[column] = generator.generate_data(column_type, nullable)

        return record

    def generate_records(
        self, table_schema: Dict[str, Dict[str, str]], num_records: int = 10
    ) -> List[Dict[str, Any]]:
        """
        Generate multiple records

        Args:
            table_schema (Dict): Dictionary of column definitions
            num_records (int): Number of records to generate

        Returns:
            List of generated records
        """
        return [self.generate_record(table_schema) for _ in range(num_records)]
