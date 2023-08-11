FROM python:3.11-alpine

WORKDIR /app

RUN apk add --no-cache openssh

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "cisco_collector.py"]
