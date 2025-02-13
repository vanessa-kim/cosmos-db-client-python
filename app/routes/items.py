# API 라우트 (Cosmos DB 데이터 조회)
from fastapi import APIRouter
from app.database import container

router = APIRouter()

@router.get("/items")
def fetch_all_items():
    query = "SELECT * FROM c"
    items = list(container.query_items(query, enable_cross_partition_query=True))
    return {"items": items}
