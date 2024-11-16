FROM python:3.12

COPY . .

RUN pip install poetry 

RUN poetry install

EXPOSE 8000

CMD ["poetry", "run", "task", "prod"]
