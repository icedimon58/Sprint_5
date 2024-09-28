from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from helps import AdditionalFunctions
from tests.page_locators import PageLocators


class TestDifferentAutorisationsMethod:

    def test_login_from_login_button(self, driver):
        drv = AdditionalFunctions().get_autorisation_on_site_from_login_button(driver)
        assert PageLocators.URL == drv.current_url

    def test_login_from_cabinet(self, driver):
        driver.find_element(*PageLocators.KABINET_LOCATOR).click()
        AdditionalFunctions().get_autorisation(driver)
        assert PageLocators.URL == driver.current_url

    def test_login_from_restore_password_button(self, driver):
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(
            PageLocators.ENTRANCE_BUTTON)).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(
            PageLocators.RESTORE_PSWD_BUTTON)).click()
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(
            PageLocators.BACK_TO_LOGIN_BUTTON)).click()
        assert PageLocators.LOGIN_PAGE == driver.current_url
