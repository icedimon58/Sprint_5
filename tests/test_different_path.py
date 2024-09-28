from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from helps import AdditionalFunctions
from tests.page_locators import PageLocators


class TestDifferentPagePath:
    def test_path_to_cabinet(self, driver):
        drv = AdditionalFunctions().get_autorisation_on_site_from_login_button(driver)
        WebDriverWait(drv, 5).until(expected_conditions.element_to_be_clickable(PageLocators.KABINET_LOCATOR)).click()
        WebDriverWait(drv, 5).until(expected_conditions.element_to_be_clickable(PageLocators.EXIT_BUTTON)).click()
        assert PageLocators.PROFILE_URL == drv.current_url

    def test_path_to_constructor_from_cabinet(self, driver):
        drv = AdditionalFunctions().get_autorisation_on_site_from_login_button(driver)
        drv.find_element(*PageLocators.KABINET_LOCATOR).click()
        drv.find_element(*PageLocators.CONSTRUCTOR_LOCATOR).click()
        assert drv.find_element(*PageLocators.CONSTRUCTOR_TEXT).text == 'Соберите бургер'

    def test_path_to_logo_from_cabinet(self, driver):
        drv = AdditionalFunctions().get_autorisation_on_site_from_login_button(driver)
        drv.find_element(*PageLocators.KABINET_LOCATOR).click()
        drv.find_element(*PageLocators.LOGO_BURGER).click()
        assert PageLocators.URL == drv.current_url

    def test_exit_from_account(self, driver):
        drv = AdditionalFunctions().get_autorisation_on_site_from_login_button(driver)
        WebDriverWait(drv, 10).until(
            expected_conditions.visibility_of_element_located(PageLocators.KABINET_LOCATOR)).click()
        WebDriverWait(drv, 10).until(
            expected_conditions.visibility_of_element_located(PageLocators.EXIT_BUTTON)).click()
        WebDriverWait(drv, 10).until(
            expected_conditions.visibility_of_element_located(PageLocators.REGISTRATION_BUTTON))
        assert PageLocators.LOGIN_PAGE == drv.current_url

    def test_stuffing_button(self, driver):
        driver.find_element(*PageLocators.SPIN_STUFFINN_BUTTON).click()
        assert driver.find_element(*PageLocators.SPIN_BUTTONS_URL).text == 'Начинки'

    def test_souce_button(self, driver):
        driver.find_element(*PageLocators.SPIN_SOUCES_BUTTON).click()
        assert driver.find_element(*PageLocators.SPIN_BUTTONS_URL).text == 'Соусы'

    def test_bread_button(self, driver):
        driver.find_element(*PageLocators.SPIN_SOUCES_BUTTON).click()
        driver.find_element(*PageLocators.SPIN_BREAD_BUTTON).click()
        assert driver.find_element(*PageLocators.SPIN_BUTTONS_URL).text == 'Булки'
