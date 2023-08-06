from .config import Config
from bs4 import BeautifulSoup

import re
import requests

class Scrap(Config):

    title = None
    price = None
    ref_price = None
    down_ratio = 0

    def __init__(self, product_id):
        self.product_id = product_id
        self.product_url = self.p_url.format(product_id)
        self.html = requests.get(url=self.product_url, headers=self.header).text
        self.soup = BeautifulSoup(self.html, "html.parser")
        self.__get_title()
        self.__get_images_urls()
        self.__get_price()
        self.__get_ref_proce()
        self.__get_down_ratio()

    def __get_title(self):
        element = self.soup.find('span', id='productTitle')
        if element:
            self.title = element.get_text().replace('\n', '').replace('  ', '')

    def __get_images_urls(self):
        url_list = []
        for element in self.soup.find_all("img"):
            image_url = element.get('src')
            if 'US40' in image_url:
                url_list.append(image_url.replace('US40', 'AC'))
        self.img_list = url_list

    def __get_price(self):
        for price_class in self.price_classes:
            element = self.soup.find('span', class_=price_class)
            if element:
                self.price = int(element.get_text().replace('￥', '').replace(',', ''))

    def __get_ref_proce(self):
        element = self.soup.find('span', class_='priceBlockStrikePriceString')
        if element:
            self.ref_price = int(element.get_text().replace('￥', '').replace(',', ''))

    def __get_down_ratio(self):
        element = self.soup.find('td', class_='priceBlockSavingsString')
        if element:
            pattern = r'￥(.*)\((.*)\%\)'
            string = element.get_text().replace(' ', '').replace('\n', '')
            self.down_ratio = int(re.match(pattern, string).group(2))
