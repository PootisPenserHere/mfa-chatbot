FROM python:3.8-alpine
LABEL maintainer = "Jose Pablo Aramburo <josepablo.aramburo@laziness.rocks>"

ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY requirements.txt .

RUN apk --no-cache add tzdata && \
    apk --no-cache --virtual .build-deps add gcc musl-dev libffi-dev openssl-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del .build-deps

RUN addgroup -S slothgroup && adduser -S container_sloth -G slothgroup
USER container_sloth

COPY . .

HEALTHCHECK --interval=10s --timeout=2s --start-period=15s \
    CMD wget --quiet --tries=1 --spider http://localhost:$PORT/health-check || exit 1

CMD gunicorn -b 0.0.0.0:$PORT --reload app:app
