FROM python:3.11.0-alpine3.16

ENV GID 1001
ENV UID 1001
ENV USER dockeruser
ENV PATH=/home/${USER}/.local/bin:${PATH}

# We are going to run as a non-root user
RUN apk add --no-cache shadow
RUN groupadd -g ${GID} ${USER} && useradd -g ${GID} -u ${UID} -m ${USER}

WORKDIR /app
COPY . /app
RUN chown -R ${USER}:${USER} /app

# We want to install the pip package as the non-root user
USER ${USER}
RUN pip install --user .
WORKDIR /home/${USER}

# Only root can delete the /app directory itself
USER root
RUN rm -rf /app

# Switch back to the non-root user to run our program
USER ${USER}
ENTRYPOINT ["py-pinyin-txt"]
