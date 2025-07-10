from browseruse.browser import Browser
from utils.config_loader import config
from utils.logger import logger

class BrowserUseRunner:
    def __init__(self):
        self.browser = Browser(browser=config['browser'], headless=config['headless'])

    def open_url(self, url):
        logger.info(f"Opening URL: {url}")
        self.browser.navigate(url)

    def quit(self):
        self.browser.quit()