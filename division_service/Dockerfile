FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY division_service.py .

EXPOSE 8004

CMD ["uvicorn", "division_service:app", "--host", "0.0.0.0", "--port", "8004"]
