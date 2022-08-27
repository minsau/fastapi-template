FROM python:3.10.5-slim-bullseye

RUN groupadd -g 1337 app && \
    useradd -m -d /opt/app -u 1337 -g app app

ENV PYTHONPATH=${PYTHONPATH}:${PWD} 

# TODO: Improve this to install dev dependencies just in development
RUN pip3 install poetry
WORKDIR /temp
ADD pyproject.toml /temp/pyproject.toml 
RUN poetry config virtualenvs.create false

RUN poetry install

USER app
WORKDIR /opt/app
RUN ls -la
ENV PATH /opt/app/.local/bin:$PATH

EXPOSE 8000

ADD --chown=app:app ./docker-entrypoint.sh /
RUN ["chmod", "+x", "/docker-entrypoint.sh"]

ENTRYPOINT ["/docker-entrypoint.sh"]