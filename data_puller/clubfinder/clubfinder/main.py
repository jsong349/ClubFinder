import sys
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/mnt/c/Users/Vaskar/Documents/Projects/ClubFinder/data_puller/clubfinder/clubfinder/spiders')

from spiders.club_spider import MySpider
from scrapy.crawler import CrawlerProcess


def main():

    start_urls = ['https://westernu.campuslabs.ca/engage/organizations']

    process = CrawlerProcess()
    process.crawl(MySpider, start_urls=start_urls)
    process.start()


if __name__ == "__main__":
    main()
