FROM python:3.9-alpine
LABEL maintainer="Artur Leśnik"

RUN mkdir -v /app

ADD endpoint /app/endpoint
ADD .env /app
ADD main.py /app

EXPOSE 8888

WORKDIR /app

RUN pip install tornado
RUN pip install pillow
RUN pip install python-dotenv

CMD ["python", "main.py"]