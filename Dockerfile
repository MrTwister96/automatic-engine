FROM python:3.8.9-buster

WORKDIR /opt/app

COPY . .

RUN pip install -r requirements.txt

CMD ["gunicorn", "covid_tracking.wsgi", "-b", "0.0.0.0:8000"]