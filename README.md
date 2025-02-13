# cosmos-db-client-python

FastAPI를 사용해서 Cosmos DB 데이터를 조회하는 파이썬 어플리케이션
- FastAPI가 기본적으로 제공하는 Swagger UI(/docs)를 통해 API 테스트 가능 
------
## API 어플리케이션 로컬에서 실행 방법
1. git repo를 로컬에 clone
2. git repo를 다운받은 폴더의 root path로 터미널 이동
3. 가상 환경 실행
```
source venv/bin/activate
```

4. 환경 변수 설정
```
export COSMOS_DB_ENDPOINT="{{ Cosmos DB Endpoint 실제 값 추가 }}"
export COSMOS_DB_KEY="{{ Cosmos DB 인증 키 실제 값 추가 }}"
export COSMOS_DB_DATABASE="db_conversation_history"
export COSMOS_DB_CONTAINER="conversations"
```
5. dependencies libraries 설치
```
pip install --break-system-packages -r requirements.txt                              
```
6. 앱 실행
```
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload                             
```
7. 로컬에서 브라우저에 `http://0.0.0.0:8000/` 입력


------
## 어플리케이션 테스트
하단의 문구가 화면이 뜨면 정상 동작
```
{"message":"FastAPI + Cosmos DB 클라이언트 실행 중!"}
```

db item 조회: url주소에 `/items`를 덧붙이면 json 데이터 조회
```
http://0.0.0.0:8000/items
```