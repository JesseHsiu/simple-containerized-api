FROM python:3.7.2

COPY ./app.py ./

RUN pip install flask

CMD env FLASK_APP=app.py flask run --host=0.0.0.0