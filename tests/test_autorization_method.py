from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from tests.page_locators import PageLocators
from data import PageUrls


class TestDifferentAutorisationsMethod:

    def test_login_from_login_button(self, driver):
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located(
            PageLocators.ENTRANCE_BUTTON)).click()
        driver.find_element(*PageLocators.MAIL).send_keys('1q2w3e@yandex.ru')
        driver.find_element(*PageLocators.PASSWORD_BUTTON).send_keys('1q2w3e')
        driver.find_element(*PageLocators.AUTORISATION_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PageLocators.SPIN_STUFFINN_BUTTON))
        assert PageUrls.URL == driver.current_url

    def test_login_from_cabinet(self, driver):
        driver.find_element(*PageLocators.KABINET_LOCATOR).click()
        driver.find_element(*PageLocators.MAIL).send_keys('1q2w3e@yandex.ru')
        driver.find_element(*PageLocators.PASSWORD_BUTTON).send_keys('1q2w3e')
        driver.find_element(*PageLocators.AUTORISATION_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PageLocators.SPIN_STUFFINN_BUTTON))
        assert PageUrls.URL == driver.current_url

    def test_login_from_restore_password_button(self, driver):
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(
            PageLocators.ENTRANCE_BUTTON)).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(
            PageLocators.RESTORE_PSWD_BUTTON)).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(
            PageLocators.BACK_TO_LOGIN_BUTTON)).click()
        assert PageUrls.LOGIN_PAGE == driver.current_url
