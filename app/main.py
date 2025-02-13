# FastAPI 서버 실행 파일
from azure.core.exceptions import AzureError
from azure.cosmos import CosmosClient, PartitionKey

from fastapi import FastAPI
from app.routes import items

app = FastAPI()

# 라우터 등록
app.include_router(items.router)

@app.get("/")
def home():
    return {"message": "FastAPI + Cosmos DB 클라이언트 실행 중!"}

# 실행 명령어
# uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload