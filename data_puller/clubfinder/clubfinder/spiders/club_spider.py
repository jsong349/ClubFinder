# -*- coding: utf-8 -*-
import scrapy
import csv
from scrapy.selector import Selector


# output from url_scraper
url = ['https://westernu.campuslabs.ca/engage/organizations']

class MySpider(scrapy.Spider):
    name = 'westernu'


    def parse(self, response):
        sel = Selector(response)

        print("START")
        print(response)
        all_the_books = response.xpath('//div[@style]')
        print(all_the_books)
        print(len(all_the_books))

        for book in all_the_books:
            title = book.xpath(".//span[@class='a-size-medium a-color-base a-text-normal']/text()").extract_first()
            author = book.css(".a-color-secondary .a-size-base:nth-child(2)").css("::text").extract_first()
            price = book.css(".a-price-whole::text").extract_first(default='0')

            row = [title, price, author]
            # Open file in append mode
            with open("../data.csv", 'a+', newline='') as write_obj:
                # Create a writer object from csv module
                csv_writer = csv.writer(write_obj)
                # Add contents of list as last row in the csv file
                csv_writer.writerow(row)
