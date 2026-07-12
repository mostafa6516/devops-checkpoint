FROM python:3.11-slim

WORKDIR /app

COPY file.py .

CMD ["python3", "file.py"]
