FROM python:3.12

WORKDIR /a2/api

COPY ./requirements.txt /a2/api/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /a2/api/requirements.txt

COPY . /a2/api/

WORKDIR /a2

ENV PYTHONPATH=.

EXPOSE 8000

CMD ["python", "api/src/main.py"]
