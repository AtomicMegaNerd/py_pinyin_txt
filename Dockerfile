FROM python:3.9.5-slim

WORKDIR /app
COPY . /app
RUN pip install .
RUN py-pinyin-txt --help
WORKDIR /
RUN rm -rf /app

ENTRYPOINT ["py-pinyin-txt"]
