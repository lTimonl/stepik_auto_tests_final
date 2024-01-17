from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage():
    def __init__(self, browser, url):
        self.browser=browser
        self.url=url
    def open(self):
        self.browser.get(self.url)
        #return self.browser.get(self.url) #изначальный вариант, но вроде как возвращать не нужно (тупо открываем не зачем записывать)
            
