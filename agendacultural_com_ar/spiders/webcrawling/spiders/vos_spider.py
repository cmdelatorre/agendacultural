from django.utils import datetime_safe

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
            start_date = None
            end_date = None
            venue = None
            time = None
            for x in e.select('.//div[contains(@class, "lineaDatos")]'):
                line = x.select('./strong/text()').extract()[0]
                data = x.select('./span/text()').extract()[0]
                if 'Comienza:' in line:
                    start_date = data
                elif 'Termina:' in line:
                    end_date = data
                elif 'Lugar y Hora:' in line:
                    try:
                        venue, time = self.extract_venue_time(data)
                    except Exception, e:
                        print "Problem with venue_time in ", event, line, data
                        event['end_time'] = datetime_safe.datetime.min
                    
            event['venue'] = venue
            
            try:
                event['start_time'] = self.build_date_time(start_date, time)
            except Exception, e:
                print "Problem with start_time in ", event, start_date, time
                event['start_time'] = datetime_safe.datetime.min
            try:
                event['end_time'] = self.build_date_time(end_date, time)
            except Exception, e:
                print "Problem with end_time in ", event, start_date, time
                event['end_time'] = datetime_safe.datetime.min
            # artists
            # tickets             
            event_items.append(event)
        
        return event_items

    def parse_start_url(self, response):
        return self.parse_events_list(response)

    def extract_venue_time(self, data):
        """Extract the venue name and the hour of the event from a string that's
        like 'Teatro Luxor | 21.30'"""
        chunks = data.split('|')
        venue = chunks[0].strip()
        time = chunks[1].strip()
        return venue, time

    def build_date_time(self, date, time):
        """Build a datetime object from the given strings. The date is something
        like 'Jueves 11 de julio 2013' and the time '21.30'."""
        month_names = ['enero', 'febrero', 'marzo', 'abril', 'mayo', 'junio', 
                       'julio', 'agosto', 'septiembre', 'octubre', 'noviembre',
                       'diciembre']
        day_str_to_int = dict(zip(month_names, range(len(month_names))))
        _, d, _, m, a = date.split()
        m = day_str_to_int[m]
        a, m, d = map(int, (a, m ,d))
        hh = 0
        mm = 0
        time = time.split('.')
        if len(time) == 1:
            hh = int(time[0])
            mm = 0
        elif len(time) == 2:
            hh, mm = map(int, time) 
        
        return datetime_safe.datetime(a, m, d, hh, mm)


