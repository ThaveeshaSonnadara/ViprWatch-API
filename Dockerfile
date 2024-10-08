FROM python:3.9-slim

ENV PYTHONBUFFERED True

ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

RUN pip install --no-cache-dir --upgrade pip
# Install production dependencies
RUN pip install --no-cache-dir -r requirements.txt

CMD exec gunicorn --bind :$PORT --workers 4 --threads 8 --timeout 0 app:app