from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from utils.config import BASE_URL


class CheckboxPage(BasePage):
    URL = BASE_URL + "checkbox-demo"

    # Multiple Checkbox Demo section - checkboxes are ex1-check1, ex1-check2, ...
    CHECK_ALL_BUTTON = (By.ID, "box")

    def open(self):
        self.navigate_to(self.URL)

    def _checkbox(self, index):
        locator = (By.ID, f"ex1-check{index}")
        return self.wait_for_element(locator)

    def check_option(self, index):
        box = self._checkbox(index)
        if not box.is_selected():
            box.click()

    def uncheck_option(self, index):
        box = self._checkbox(index)
        if box.is_selected():
            box.click()

    def is_option_checked(self, index):
        return self._checkbox(index).is_selected()

    def check_all(self):
        self.wait_for_clickable(self.CHECK_ALL_BUTTON).click()
