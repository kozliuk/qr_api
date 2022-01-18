FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN apt update && apt install make
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
