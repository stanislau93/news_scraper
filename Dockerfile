# See https://hub.docker.com/r/library/python/
FROM python

RUN apt-get update && apt-get upgrade -y
RUN pip install --upgrade pip
WORKDIR /app

RUN ls -ll

COPY ./requirements.txt /app/requirements.txt

RUN pip install -r requirements.txt

ADD . /app

#CMD ["scrapy crawl", "news.py"]
CMD scrapy runspider newsscraper.py
