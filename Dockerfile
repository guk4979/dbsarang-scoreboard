# Dockerfile
FROM python:3.9.19

# 작업 디렉토리 설정
WORKDIR /app

# 의존성 복사 및 설치
COPY requirement.txt .
RUN pip install --upgrade pip 
RUN pip install --no-cache-dir -r requirement.txt

# 소스 코드 복사
COPY . .

# 포트 노출
EXPOSE 8000

# Django 애플리케이션 실행
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.asgi:application"]
