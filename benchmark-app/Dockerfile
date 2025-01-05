# 這裡使用 Python 3.9 (或其他版本都行)
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY app.py /app/

# 預設ENV
ENV APP_TYPE=default

EXPOSE 8080
CMD ["python", "app.py"]
