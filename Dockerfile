FROM python:3.10.9-alpine3.17

WORKDIR /flask_app

COPY requirements.txt requirements.txt

COPY . .

RUN pip3 install -r requirements.txt

CMD ["python3", "app.py"]