FROM python:3

ENV PYTHONUNBUFFERED=1

WORKDIR /usr/src/app

COPY req.txt .
COPY entrypoint.sh .

RUN pip install -r req.txt
RUN chmod +x entrypoint.sh

COPY ../kavKev_Site/ .

ENTRYPOINT ["/usr/src/app/entrypoint.sh"]