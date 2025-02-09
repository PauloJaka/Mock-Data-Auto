from typing import Any, Dict, List

from app.models.schemas import TableSchemaRequest
from app.services.data_generator import DataGenerator
from fastapi import APIRouter, HTTPException

router = APIRouter()
data_generator = DataGenerator()


@router.post("/generate-data/")
async def generate_fake_data(request: TableSchemaRequest) -> List[Dict[str, Any]]:
    """
    Generate fake data based on provided table schema
    """
    try:
        records = data_generator.generate_records(request.schema, request.num_records)
        return records
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
