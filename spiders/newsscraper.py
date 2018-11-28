#! /path/to/ENV/bin/python
import scrapy
from article_spider import ArticleSpider
import news_scraper.newsscraper_service as service

class NewsFeedSpider(scrapy.Spider):
  name = 'news'
  page_number = 1
  article_scraper = ArticleSpider()

  start_urls = ['http://gvardeysk.gov39.ru/news/']

  def parse(self, response):
    service.initialize()  
    for newsElement in response.xpath("//*[@id = 'news_list']/table"):
      text = newsElement.xpath(".//span[@class='news-preview-text']/div//text()").extract_first()

      if text is None:
        continue
      
      words = service.cleanText(text).split()
      
      articlePageLink = newsElement.xpath(".//a[starts-with(@href,'/news/detail.php?ELEMENT_ID')]").extract_first() 
      
      yield {
        'day': newsElement.xpath(".//font[@class='day']//text()").extract_first(),
        'month': service.parseMonth(newsElement.xpath(".//font[@class='month']//text()").extract_first().lower(), 'rus1'),
        'title': newsElement.xpath(".//a[@class='news_header']//text()").extract_first(),
        'text': newsElement.xpath(".//span[@class='news-preview-text']/div//text()").extract_first(),
      }

      link_to_article = newsElement.xpath(".//a[@class='news_header']/@href").extract_first()

      if link_to_article is not None:
        print("FOLLOW " + link_to_article)
        yield response.follow(link_to_article, self.article_scraper.parse)
      else:
        print("NO ARTICLE LINK FOUND FOR " + link_to_article)

    self.page_number += 1    
    next_page = response.xpath("//a[@href = '/news/?PAGEN_1=" + str(self.page_number) + "']/@href").extract_first()

    if next_page is not None:
      pass
      #yield response.follow(next_page, self.parse)
    else:
      print ("finished on page " + str(self.page_number - 1))
