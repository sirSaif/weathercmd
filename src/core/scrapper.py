from selenium import webdriver


class Scrapper:
    def __init__(self, base_url):
        self._driver = webdriver.PhantomJS()
        self.base_url = base_url

    def fetch_data(self, forecast=None, area=None):
        url = self.base_url
        self._driver.get(url)
        if self._driver.title == '404 Not Found':
            error_message = 'Could not find the area that you searching for'
            raise Exception(error_message)
        return self._driver.page_source

