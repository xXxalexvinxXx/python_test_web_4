import yaml
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

base_url = testdata["address"]


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.base_url = base_url

    def find_element(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(
            EC.presence_of_element_located(locator),
            message=f"Can't find element by locator {locator}",
        )

    def get_element_property(self, locator, prop):
        element = self.find_element(locator)
        return element.value_of_css_property(prop)

    def go_to_site(self):
        return self.driver.get(self.base_url)
