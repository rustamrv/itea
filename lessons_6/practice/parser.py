 
from requests import get, exceptions
from bs4 import BeautifulSoup
import re


class Parser:

    def __init__(self, url: str):
        self.__url = url
        self.__http = None
        self.__cont = None
        self.__soap = None
        self.__html = None

    def check_valid(self) -> bool:
        try:
            self.__http = get(self.__url)
            self.__cont = self.__http.content
            self.__soap = BeautifulSoup(self.__cont, 'html.parser')
            self.__html = self.__soap.prettify()
        except exceptions.BaseHTTPError as err1:
            print(err1)
        except exceptions.MissingSchema as err2:
            print(err2)
        else:
            return True
        return False

    def get_html(self) -> str:
        return self.__html

    def get_weather(self):
        target_div = self.__soap.select('.region_weather')[0]
        result = target_div.select('.table')[0]
        target_name = result.find_all('a')
        name = [re.sub(r'\s+', ' ', cell.text) for cell in target_name]

        target_cells = result.find_all('span', attrs={'class': 'rw_tmp'})
        temperature = [re.sub(r'\s+', ' ', cell.text) for cell in target_cells]
        for i in range(len(name)):
            print(name[i], temperature[i])