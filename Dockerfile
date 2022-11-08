FROM python:3.11.0-alpine3.16 as base

# Setup env
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONFAULTHANDLER 1

FROM base as builder

ENV PATH=/home/${USER}/.local/bin:${PATH}
ENV PIP_VER 22.3.1
ENV PIPENV_VER 2022.11.5

RUN apk add --no-cache musl-dev gcc \
    && rm -rf /var/cache/apk/*

COPY Pipfile .
COPY Pipfile.lock .

RUN pip install --upgrade "pip==${PIP_VER}"
RUN pip install "pipenv==${PIPENV_VER}"
RUN PIPENV_VENV_IN_PROJECT=1 pipenv install --deploy

FROM base as runtime

ENV GID 1001
ENV UID 1001
ENV USER dockeruser
ENV PATH="/.venv/bin:$PATH"

WORKDIR /data
COPY --from=builder /.venv /.venv
COPY py_pinyin_txt .
RUN adduser -D ${USER} && chown -R ${USER}:${USER} /data

# Switch back to the non-root user to run our program
USER ${USER}
ENTRYPOINT ["python", "-m", "py_pinyin_txt"]
