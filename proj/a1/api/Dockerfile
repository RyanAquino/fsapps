FROM python:3.12-alpine

LABEL authors="ryan"

RUN apk update

RUN apk add gcc musl-dev mariadb-connector-c-dev

WORKDIR /a1

COPY ./requirements.txt /a1/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /a1/requirements.txt

COPY . /a1/

CMD ["python", "src/api.py"]
