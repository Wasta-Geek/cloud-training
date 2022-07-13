FROM tiangolo/uvicorn-gunicorn-fastapi:python3.9-alpine3.14

ARG PORT=40001

ENV PORT ${PORT}

COPY app/requirements.txt /app

RUN pip3 install -r /app/requirements.txt

COPY ./app /app

CMD uvicorn main:app --host 0.0.0.0 --port ${PORT}