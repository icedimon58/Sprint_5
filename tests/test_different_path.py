from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from tests.page_locators import PageLocators
from data import PageUrls

class TestDifferentPagePath:
    def test_path_to_cabinet(self, driver):
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located(
            PageLocators.ENTRANCE_BUTTON)).click()
        driver.find_element(*PageLocators.MAIL).send_keys('1q2w3e@yandex.ru')
        driver.find_element(*PageLocators.PASSWORD_BUTTON).send_keys('1q2w3e')
        driver.find_element(*PageLocators.AUTORISATION_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PageLocators.SPIN_STUFFINN_BUTTON))
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(PageLocators.KABINET_LOCATOR)).click()
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(PageLocators.EXIT_BUTTON)).click()
        assert PageUrls.PROFILE_URL == driver.current_url

    def test_path_to_constructor_from_cabinet(self, driver):
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located(
            PageLocators.ENTRANCE_BUTTON)).click()
        driver.find_element(*PageLocators.MAIL).send_keys('1q2w3e@yandex.ru')
        driver.find_element(*PageLocators.PASSWORD_BUTTON).send_keys('1q2w3e')
        driver.find_element(*PageLocators.AUTORISATION_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PageLocators.SPIN_STUFFINN_BUTTON))
        driver.find_element(*PageLocators.KABINET_LOCATOR).click()
        driver.find_element(*PageLocators.CONSTRUCTOR_LOCATOR).click()
        assert driver.find_element(*PageLocators.CONSTRUCTOR_TEXT).text == 'Соберите бургер'

    def test_path_to_logo_from_cabinet(self, driver):
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located(
            PageLocators.ENTRANCE_BUTTON)).click()
        driver.find_element(*PageLocators.MAIL).send_keys('1q2w3e@yandex.ru')
        driver.find_element(*PageLocators.PASSWORD_BUTTON).send_keys('1q2w3e')
        driver.find_element(*PageLocators.AUTORISATION_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PageLocators.SPIN_STUFFINN_BUTTON))
        driver.find_element(*PageLocators.KABINET_LOCATOR).click()
        driver.find_element(*PageLocators.LOGO_BURGER).click()
        assert PageUrls.URL == driver.current_url

    def test_exit_from_account(self, driver):
        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located(
            PageLocators.ENTRANCE_BUTTON)).click()
        driver.find_element(*PageLocators.MAIL).send_keys('1q2w3e@yandex.ru')
        driver.find_element(*PageLocators.PASSWORD_BUTTON).send_keys('1q2w3e')
        driver.find_element(*PageLocators.AUTORISATION_BUTTON).click()
        WebDriverWait(driver, 5).until(
            expected_conditions.visibility_of_element_located(PageLocators.SPIN_STUFFINN_BUTTON))
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(PageLocators.KABINET_LOCATOR)).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(PageLocators.EXIT_BUTTON)).click()
        WebDriverWait(driver, 10).until(
            expected_conditions.visibility_of_element_located(PageLocators.REGISTRATION_BUTTON))
        assert PageUrls.LOGIN_PAGE == driver.current_url

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
