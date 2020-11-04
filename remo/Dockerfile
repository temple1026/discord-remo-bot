FROM python:3.7.6

RUN mkdir -p /app/remo
WORKDIR /app/remo
RUN pip3 install discord pytz

COPY ./remo_main.py /app/remo/
COPY ./remoapi.py /app/remo/
COPY ./config.ini /app/remo/

CMD ["python3", "remo_main.py"]