# Cosmos DB 연결 파일
from azure.cosmos import CosmosClient
from dotenv import load_dotenv
import os

load_dotenv()  # .env 파일 로드

COSMOS_DB_ENDPOINT = os.getenv("COSMOS_DB_ENDPOINT")
COSMOS_DB_KEY = os.getenv("COSMOS_DB_KEY")
DATABASE_NAME = os.getenv("COSMOS_DB_DATABASE")
CONTAINER_NAME = os.getenv("COSMOS_DB_CONTAINER")

client = CosmosClient(COSMOS_DB_ENDPOINT, COSMOS_DB_KEY) 
database = client.get_database_client(DATABASE_NAME)
container = database.get_container_client(CONTAINER_NAME)

# --------------------------------------------------------------------------------------------------------------
# 로컬 환경변수 셋팅 (미정의시 database.py 오류 발생)
# 하단의 명령어는 로컬에서 테스트용 환경 변수 셋팅 코드 
# container apps에 api 어플리케이션 배포할 경우, 하단의 환경변수 설정해야 한다.

# export COSMOS_DB_ENDPOINT="{{ Cosmos DB Endpoint 실제 값 추가 }}"
# export COSMOS_DB_KEY="{{ Cosmos DB 인증 키 실제 값 추가 }}"
# export COSMOS_DB_DATABASE="db_conversation_history"
# export COSMOS_DB_CONTAINER="conversations"

# --------------------------------------------------------------------------------------------------------------
