import scrapy
import json
from datetime import datetime

class OlxSpider(scrapy.Spider):
    name = "olx"
    allowed_domains = ["www.olx.com.br"]
    start_urls = ["https://www.olx.com.br/imoveis/aluguel/estado-sc/florianopolis-e-regiao"]

    def parse(self, response):

        data_rents = json.loads(response.xpath('//script[@id="__NEXT_DATA__"]/text()').get())
        rents = data_rents.get('props').get('pageProps').get('ads')

        for rent in rents:

            #formatar a data que vem em padrão Unix
            date_timestamp = rent.get('date', 0)
            date_formatted = datetime.utcfromtimestamp(date_timestamp).strftime('%Y-%m-%d %H:%M:%S') if date_timestamp else ''

            yield {
                'title' : rent.get('title'),
                'price' : rent.get('price'),
                'old_price' : rent.get('oldPrice'),
                'image' : rent.get('images', '')[0].get('original', '') if rent.get('images') else '',
                'url' : rent.get('url'),
                'date' : date_formatted,
                'location' : rent.get('location'),
                'city' : rent.get('locationDetails').get('municipality', '') if rent.get('locationDetails') else '',
                'neighbourhood' : rent.get('locationDetails').get('neighbourhood', '') if rent.get('locationDetails') else '',
                'uf' : rent.get('locationDetails').get('uf', '') if rent.get('locationDetails') else '',
                'category' : rent.get('category')
            }

        for page in range(2, 200):
            yield scrapy.Request(f'https://www.olx.com.br/imoveis/aluguel/estado-sc/florianopolis-e-regiao?o={page}', self.parse)