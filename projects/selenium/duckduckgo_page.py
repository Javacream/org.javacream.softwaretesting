from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.firefox.options import Options
from selenium.webdriver import Firefox as Browser

class SearchPage:
    SEARCH_INPUT_SELECTION = (By.ID, "searchbox_input")
    def __init__(self):
        self.url = 'https://duckduckgo.com/'
        self.driver = Browser()
    def close(self):
        self.driver.quit()

    def get_title(self):
        self.driver.get(self.url)
        return self.driver.title   


    def make_search(self, search_text):
        self.driver.get(self.url)
        search_input = self.driver.find_element(by=By.ID, value="searchbox_input")
        search_button = self.driver.find_element(by=By.XPATH, value="//*[@id='searchbox_homepage']//*[@type='submit']")
        search_input.send_keys(search_text)
        search_button.click()
        self.driver.save_screenshot("results.png")

 