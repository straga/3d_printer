FROM python:3.7-slim-buster

USER root

RUN pip3 install tornado==6.1.0 pyserial==3.4

RUN apt-get update && apt-get install -y  --no-install-recommends\
        python3-dev build-essential libjpeg-dev libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev \
    && rm -rf /var/lib/apt/lists/* \
    && apt-get purge -y --auto-remove \
    && apt-get autoclean -y

RUN pip3 install pillow==8.0.1

RUN apt-get autoremove -y python3-dev build-essential libssl-dev libffi-dev libxml2-dev libxslt1-dev zlib1g-dev
RUN apt-get autoclean -y

COPY moonraker/run.sh /
RUN chmod +x run.sh

CMD ["./run.sh"]