FROM python:3.7

WORKDIR /usr/src/app

RUN pip install mysql-connector-python

ADD ./concentrator/server.py .

EXPOSE 1111

CMD [ "python", "./server.py" ]