FROM python:3.8-slim-buster

RUN pip install pipenv

WORKDIR /usr/src/app

COPY . .

RUN pipenv install --system --deploy --ignore-pipfile

CMD [ "python", "./app.py" ]
