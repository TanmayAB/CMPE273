FROM python:2.7.13
MAINTAINER Tanmay "tabhatt1993@gmail.com"
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
cmd ["app.py"]
