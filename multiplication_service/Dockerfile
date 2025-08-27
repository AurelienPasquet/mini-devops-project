FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY multiplication_service.py .

EXPOSE 8003

CMD ["uvicorn", "multiplication_service:app", "--host", "0.0.0.0", "--port", "8003"]
