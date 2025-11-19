FROM python:3.11-slim

WORKDIR /app

# Copy requirements first to leverage Docker layer cache
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy only client code to keep image small
COPY client-hf/ ./client

# Unset Python output buffering
ENV PYTHONUNBUFFERED=1

WORKDIR /app/client

CMD ["python", "count_r_client.py"]
