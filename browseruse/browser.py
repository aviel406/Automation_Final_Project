from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.config_loader import config

class Browser:
    def __init__(self, browser='chrome', headless=True):
        if browser == 'chrome':
            options = Options()
            if headless:
                options.add_argument('--headless')
            self.driver = webdriver.Chrome(options=options)
        else:
            raise ValueError("Unsupported browser")

    def navigate(self, url):
        self.driver.get(url)

    def quit(self):
        self.driver.quit()