FROM python:3.7
COPY requirements.txt /
RUN pip install -r requirements.txt
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . .
RUN python -m pytest .
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 app:app
