FROM python:3.7.3

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

RUN apt-get update
RUN apt-get install libsasl2-dev python-dev libldap2-dev libssl-dev -y

WORKDIR /

ADD requirements.txt /
RUN pip install --no-cache-dir -r requirements.txt

ADD app /app
ADD tests /tests
ADD run_server.sh /

WORKDIR /


EXPOSE 8080