import re
import scrapy
from news_scraper.items import ArticleItem
from news_scraper.settings import PROJECT_DIR

class ArticleSpider(scrapy.Spider):
  name = 'articles'

  def parse(self, response):
    page_id = re.search(r'ELEMENT_ID=(\d+)', response.url).group(1)
    title = response.css('h1').extract_first()
    article_element = response.xpath("//div[@class='news-detail']")

    text_parts = article_element.xpath(".//text()").extract()
    text_parts = [part.strip() for part in text_parts]
    text = ''.join(text_parts)

    image_url = article_element.xpath(".//img/@src").extract_first()
    image_url = ''.join(['http://gvardeysk.gov39.ru', image_url])

    item = ArticleItem()
    item['image_urls'] = [image_url]
    item['text'] = text

    f = open(PROJECT_DIR + "assets/articles/article_" + str(page_id) + ".txt","w")
    f.write(text)
    f.close()

    yield item