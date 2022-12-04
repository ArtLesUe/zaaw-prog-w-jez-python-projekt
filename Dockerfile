FROM python:3.9-alpine
MAINTAINER "Artur Leśnik"

RUN mkdir -v /app

ADD endpoint /app/endpoint
ADD modules /app/modules
ADD .env /app
ADD main.py /app

EXPOSE 8888

WORKDIR /app

RUN pip install tornado
RUN pip install pillow
RUN pip install python-dotenv
RUN pip install sympy

CMD ["python", "main.py"]