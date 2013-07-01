# Scrapy settings for webcrawling project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#
def setup_django_env(path):
    import imp, os
    from django.core.management import setup_environ

    f, filename, desc = imp.find_module('settings', [path])
    project = imp.load_module('settings', f, filename, desc)       

    setup_environ(project)

setup_django_env('../agendacultural_com_ar/')


BOT_NAME = 'webcrawling'

SPIDER_MODULES = ['webcrawling.spiders']
NEWSPIDER_MODULE = 'webcrawling.spiders'

ITEM_PIPELINES = [
				  'webcrawling.pipelines.ToAgendaDB',
				  #'webcrawling.pipeline.AddURL',
				  ]

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'webcrawling (+http://www.yourdomain.com)'
