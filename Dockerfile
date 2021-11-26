FROM python:3
MAINTAINER  Boiko Lev <lev201611@gmail.com>
ENV PYTHONUNBUFFERED=1
WORKDIR /code
COPY req.txt /code/
RUN pip install -r req.txt
COPY ./kavKev_Site /code/