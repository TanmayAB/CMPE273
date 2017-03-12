FROM python:2.7.13
MAINTAINER Tanmay "tabhatt1993@gmail.com"
ADD ./start.sh .
COPY . /app
WORKDIR /app
RUN ls
RUN pip install -r requirements.txt
ENTRYPOINT ["/bin/bash", "-c", "/start.sh ${*}", "--"]
