from scrapy.crawler import CrawlerProcess
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings
from scrapy.settings import Settings

from scrapy_app.crawler.spiders import TassSpider


def crawl_spider(spider_name:str='tass'):
    configure_logging({'LOG_FORMAT' : '%(levelname)s: %(message)s'})

    if (spider_name == 'tass'):
        spider = TassSpider
    else:
        raise NotImplementedError()

    settings = Settings()
    settings_module_path = 'scrapy_app.settings'
    settings.setmodule(settings_module_path, priority='project')

    process = CrawlerProcess(settings)
    process.crawl(spider)
    process.start()

if __name__ == '__main__':
    crawl_spider('tass')
