FROM python:3.12-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -U pip

RUN pip install --no-cache-dir -r requirements.txt

RUN apk -U upgrade && apk add netcat-openbsd

COPY . .

RUN chmod +x wait-for-it.sh

CMD ["pytest", "--launch_mode", "--url", "--browser", "--executor"]
