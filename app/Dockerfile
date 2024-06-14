FROM python:3.9.19-slim-bullseye

WORKDIR /usr/src/app
RUN apt-get update && apt-get install -y curl
RUN pip install --upgrade pip
RUN pip install flask
COPY app.py /usr/src/app/

ENV TARGET="Jhonnathan"

EXPOSE 8883

USER 9000:9000

CMD ["python", "/usr/src/app/app.py"]