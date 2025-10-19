FROM python:3.14-slim

WORKDIR /mapproject

RUN apt-get update && apt-get install -y build-essential && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["uvicorn", "mapproject.asgi:application", "--reload"]
