FROM python:3.8-slim

WORKDIR /code
RUN apt -y update \
    && apt -y install curl less wget jq vim build-essential \
    && apt -y clean \
    && apt -y autoremove \
    && rm -rf /var/lib/apt/lists/*
    
ENV PATH="$PATH:/root/.poetry/bin"

RUN pip install --upgrade pip \
    && curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/1.0.2/get-poetry.py | python

COPY poetry.lock pyproject.toml /code/

RUN poetry config virtualenvs.create false \
    && poetry install --no-interaction --no-ansi

EXPOSE 8080 8080

CMD [ "uvicorn", "pokemon_shakespeare.main:app", "--host", "0.0.0.0", "--port", "8080" ]

COPY . /code

ARG GIT_COMMIT=unspecified
LABEL git_commit=$GIT_COMMIT

