FROM python:3.11-slim

WORKDIR /app

# Copy requirements first to leverage Docker layer cache
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Copy only server code to keep image small
COPY server/ ./server

# Default port
EXPOSE 8000

# Unset Python output buffering
ENV PYTHONUNBUFFERED=1

WORKDIR /app/server

CMD ["python", "count_r_server.py"]
