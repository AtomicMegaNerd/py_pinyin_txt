FROM python:3.9.5-alpine3.13

WORKDIR /app
COPY . /app
RUN pip install .
WORKDIR /
RUN rm -rf /app

ENTRYPOINT ["py-pinyin-txt"]
