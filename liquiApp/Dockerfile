FROM python:3.10.4-alpine3.15
ENV PYTHONUNBUFFERED 1
WORKDIR /app
RUN apk update \
    && apk add --no-cache gcc musl-dev postgresql-dev python3-dev libffi-dev \
    && pip install --upgrade pip
COPY ./requirements.txt ./
RUN apk add mariadb-dev
RUN pip install -r requirements.txt
RUN pip install django
RUN pip install mysql-connector-python
RUN pip install mysqlclient
RUN pip install requests
COPY ./ ./
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]