FROM python:3.8-alpine
LABEL maintainer = "Jose Pablo Aramburo <josepablo.aramburo@laziness.rocks>"

ENV PYTHONUNBUFFERED 1

WORKDIR /code
COPY requirements.txt .

RUN apk --no-cache add tzdata && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

HEALTHCHECK --interval=10s --timeout=2s --start-period=15s \
    CMD wget --quiet --tries=1 --spider http://localhost:$APP_PORT/health-check || exit 1

CMD gunicorn -b 0.0.0.0:$APP_PORT --reload app:app
