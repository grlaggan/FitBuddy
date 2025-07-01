FROM python:3.13-bookworm

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /fitbuddy

RUN pip install --upgrade pip wheel poetry
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./

RUN poetry install

COPY . .

RUN chmod +x ./src/prestart.sh

ENV PYTHONPATH=/fitbuddy

ENTRYPOINT ["./src/prestart.sh"]
CMD ["python", "src/main.py"]