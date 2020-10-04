FROM python:3.8-buster

WORKDIR /tmp
COPY requirements.txt /tmp

RUN pip install --upgrade pip --no-cache-dir && \
    pip install -r requirements.txt --no-cache-dir

RUN mkdir /tmp/app
WORKDIR /tmp/app

CMD python example