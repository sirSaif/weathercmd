import os
from selenium import webdriver


class Scrapper:
    def __init__(self, base_url):
        self._phantomjs_path = "/".join(os.getcwd().split('/')[:-2]+['phantomjs', 'bin/'])
        print(self._phantomjs_path)
        self._base_url = base_url
        self._driver = webdriver.PhantomJS(executable_path=self._phantomjs_path)

    def fetch_data(self, forecast, area):
        url = self._base_url.format(forecast=forecast, area=area)
        self._driver.get(url)
        if self._driver.title == '404 Not Found':
            error_message = 'Could not find the area that you searching for'
            raise Exception(error_message)
        return self._driver.page_source


s = Scrapper("")
