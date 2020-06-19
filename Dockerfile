FROM tiangolo/uvicorn-gunicorn

MAINTAINER Ramon Ziai <ramon.ziai@uni-tuebingen.de>

ADD . /app

RUN pip install -r requirements.txt

