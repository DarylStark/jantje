
FROM python:3.9.5-slim
RUN apt-get update \
    && apt-get install gcc g++ -y \
    && apt-get clean
COPY requirements.txt /
RUN pip3 install --upgrade pip
RUN pip3 install -r /requirements.txt
COPY . /app
WORKDIR /app
ENTRYPOINT ["./gunicorn.sh"]
