# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

RUN adduser --disabled-password user
RUN chown -R user:user /code/
RUN chown -R user:user /usr/local/lib/python3.9/site-packages/
USER user
