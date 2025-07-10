from aluminum.core.driver_wrapper import DriverWrapper
from utils.config_loader import config
from utils.logger import logger

class AluminumRunner:
    def __init__(self):
        self.driver = DriverWrapper(browser=config['browser'], headless=config['headless'])

    def open_url(self, url):
        logger.info(f"Opening URL: {url}")
        self.driver.go_to(url)

    def quit(self):
        self.driver.quit()