from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

from pages.base_page import BasePage
from utils.config import BASE_URL, DEFAULT_TIMEOUT


class InputFormPage(BasePage):
    """
    Field IDs on this page have changed at least once already (LambdaTest -> TestMu AI
    rebrand), so locators here use placeholder-text matching instead of exact
    id/name attributes - more likely to survive another redesign than a guessed id.
    """

    URL = BASE_URL + "input-form-demo"

    NAME_INPUT = (By.CSS_SELECTOR, "input[placeholder*='Name' i]")
    EMAIL_INPUT = (By.CSS_SELECTOR, "input[type='email'], input[placeholder*='Email' i]")
    PHONE_INPUT = (By.CSS_SELECTOR, "input[type='tel'], input[placeholder*='Phone' i]")
    ADDRESS_INPUT = (By.CSS_SELECTOR, "textarea[placeholder*='Address' i], input[placeholder*='Address' i]")
    SUBMIT_BUTTON = (By.CSS_SELECTOR, "button[type='submit'], input[type='submit']")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, ".alert-success, .success-msg, h2")

    def open(self):
        self.navigate_to(self.URL)

    def fill_form(self, name, email, phone, address):
        self.wait_for_element(self.NAME_INPUT).send_keys(name)
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)

    def submit_form(self):
        self.wait_for_clickable(self.SUBMIT_BUTTON).click()

    def get_success_message(self):
        return self.wait_for_element(self.SUCCESS_MESSAGE).text
