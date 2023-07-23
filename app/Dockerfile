ARG PYTHON_VERSION
FROM python:${PYTHON_VERSION}-alpine

ARG POSTGRESQL_VERSION
ENV POSTGRESQL_VERSION=${POSTGRESQL_VERSION}
RUN apk add --no-cache gcc=~12.2.1 musl-dev=~1.2.4 postgresql15-dev=~${POSTGRESQL_VERSION}

WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .

WORKDIR /usr/src
CMD ["waitress-serve", "app:app"]
EXPOSE 8080
HEALTHCHECK --interval=2s CMD ["wget", "-qO", "-", "http://127.0.0.1:8080/healthz"]
