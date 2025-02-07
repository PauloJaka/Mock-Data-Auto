from pydantic import BaseModel, Field


class ColumnSchema(BaseModel):
    name: str
    type: str = Field(..., regex="^(string|integer|date|boolean)$")


class SQLRequest(BaseModel):
    table_name: str = Field(..., min_length=1)
    columns: list[ColumnSchema]
    num_rows: int = Field(gt=0, le=1000, default=5)
