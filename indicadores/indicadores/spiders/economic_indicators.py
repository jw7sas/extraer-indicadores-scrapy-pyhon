import scrapy
import datetime

class EconomicIndicators(scrapy.Spider):
    """ Spider para obtener nuestros indicadores economicos. """
    name = 'e_indicators'
    start_urls = [
        'https://www.dane.gov.co/index.php/indicadores-economicos'
    ]

    custom_settings = {
        'FEED_URI': 'indicadores_economicos.csv',
        'FEED_FORMAT': 'csv',
        'ROBOTSTXT_OBEY': True,
        'FEED_EXPORT_ENCODING': 'utf-8'
    }

    def parse(self, response):
        indicators = response.xpath('//section[contains(@class, "article-content") and @itemprop="articleBody"]//table//h2/strong/text()').getall() 
        values = response.xpath('//section[contains(@class, "article-content") and @itemprop="articleBody"]//table//h1/text()').getall()

        for ind, val in zip(indicators, values):
            info = {
                'indicador': ind,
                'valor': val,
                'fecha': datetime.date.today()
            }

            yield info