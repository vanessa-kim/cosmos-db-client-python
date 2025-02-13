# 도커 이미지 빌드 설정

# Python 3.12.9 베이스 이미지 사용
FROM python:3.12.9

# 환경 변수 로드
ENV COSMOS_DB_ENDPOINT="{{ Cosmos DB Endpoint 실제 값 추가 }}"
ENV COSMOS_DB_KEY="{{ Cosmos DB 인증 키 실제 값 추가 }}"
ENV COSMOS_DB_DATABASE="db_conversation_history"
ENV COSMOS_DB_CONTAINER="conversations"

# 작업 디렉토리 설정
WORKDIR /app


# 시스템 패키지 업데이트 및 OpenSSL 설치
RUN apt-get update && apt-get install -y \
    openssl \
    ca-certificates

    # OpenSSL 디렉토리 설정
ENV OPENSSL_DIR="/opt/homebrew/etc/openssl@3"
ENV SSL_CERT_FILE="$OPENSSL_DIR/cert.pem"
ENV SSL_CERT_DIR="$OPENSSL_DIR/certs"

# OpenSSL 심볼릭 링크 생성 (경로가 존재하지 않는 경우 대비)
RUN mkdir -p $OPENSSL_DIR && \
    ln -s /etc/ssl/certs/ca-certificates.crt $SSL_CERT_FILE

# 코드 및 인증서 복사
COPY . /app

# 인증서 등록
RUN chmod 644 /usr/local/share/ca-certificates/custom-ca.crt && \
    update-ca-certificates


# requirements.txt 복사 후 패키지 설치
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# FastAPI 실행
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
