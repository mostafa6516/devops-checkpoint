FROM python:3.11-slim

WORKDIR /app

COPY file.py .

CMD ["python2", "file.py"]
