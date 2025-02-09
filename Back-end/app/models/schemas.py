from typing import Dict

from pydantic import BaseModel


class TableSchemaRequest(BaseModel):
    schema: Dict[str, Dict[str, str]]
    num_records: int = 10
