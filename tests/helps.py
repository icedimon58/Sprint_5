import random
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tests.page_locators import PageLocators


class AdditionalFunctions:
    MAILS = ('@yandex.ru', '@bk.ru', '@mail.ru')

    def generate_password(self):
        return random.randint(100000, 999999)

    def generate_wrong_password(self):
        return random.randint(1, 99999)

    def generate_email(self):
        return f'{self.generate_password()}{random.choice(self.MAILS)}'

    def get_autorisation(self, driver):
        driver.find_element(*PageLocators.MAIL).send_keys('1q2w3e@yandex.ru')
        driver.find_element(*PageLocators.PASSWORD_BUTTON).send_keys('1q2w3e')
        driver.find_element(*PageLocators.AUTORISATION_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PageLocators.SPIN_STUFFINN_BUTTON))

    def get_autorisation_on_site_from_login_button(self, driver):
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located(
            PageLocators.ENTRANCE_BUTTON)).click()
        self.get_autorisation(driver)
        return driver
