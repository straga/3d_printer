FROM python:3.8-slim-buster

USER root
ENV MULTIDICT_NO_EXTENSIONS=1
ENV YARL_NO_EXTENSIONS=1 
RUN pip3 install aiohttp

COPY ui/run.sh /
RUN chmod +x run.sh

CMD ["./run.sh"]
