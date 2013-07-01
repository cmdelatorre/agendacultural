from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.selector import HtmlXPathSelector


from webcrawling.items import Event


event_link_pattern = r"(http\://vos\.lavoz\.com\.ar)*/buscador_eventos\?page=(\w|%)+&todos=6550"



class VosSpider(CrawlSpider):
    name = "Vos"
    allowed_domains = ["vos.lavoz.com.ar"]
    start_urls = [
        "http://vos.lavoz.com.ar/buscador_eventos?todos=6550",
    ]
    rules = [Rule(SgmlLinkExtractor(allow=[event_link_pattern]), 'parse_events_list')]

    def parse_events_list(self, response):
        hxs = HtmlXPathSelector(response)
        events_selector = hxs.select('//div[@class="Noticias"]')
        event_items = []
        for e in events_selector:
            event = Event()
            event['url'] = e.select('.//h3/a/@href').extract()[0]
            event['name'] = e.select('.//h3/a/text()').extract()[0]
            event['short_description'] = e.select(
                './/div[@class="texto"]/p/text()').extract()[0]
            # description
            # photo
            start_time = '2103-06-30 12:34'
            # end_time
            # artists
            event['venue'] = 'Mi casa'
            # tickets 
            
            event_items.append(event)
        
        return event_items

    def parse_start_url(self, response):
        return self.parse_events_list(response)

