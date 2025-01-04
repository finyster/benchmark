FROM python:3.9-slim

WORKDIR /app
COPY app.py /app/
RUN pip install flask prometheus_client

EXPOSE 8080 8000
CMD ["python", "app.py"]
