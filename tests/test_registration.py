from helps import AdditionalFunctions
from tests.page_locators import PageLocators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


class TestRegistrations:
    def test_registration_postive(self, driver):
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(
            PageLocators.ENTRANCE_BUTTON)).click()
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(
            PageLocators.REGISTRATION_BUTTON)).click()
        driver.find_element(*PageLocators.NAME_FIELD_REGISTRASTION).send_keys(AdditionalFunctions().generate_password())
        driver.find_element(*PageLocators.EMAIL_FIELD_REGISTRASTION).send_keys(AdditionalFunctions().generate_email())
        driver.find_element(*PageLocators.PWD_FIELD_REGISTRASTION).send_keys(AdditionalFunctions().generate_password())
        driver.find_element(*PageLocators.REGISTRATION_BUTTON_ON_REGISTR_PAGE).click()
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(
            PageLocators.AUTORISATION_BUTTON))
        assert PageLocators.LOGIN_PAGE == driver.current_url

    def test_registration_wrong_password(self, driver):
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(
            PageLocators.ENTRANCE_BUTTON)).click()
        WebDriverWait(driver, 2).until(expected_conditions.visibility_of_element_located(
            PageLocators.REGISTRATION_BUTTON)).click()
        driver.find_element(*PageLocators.NAME_FIELD_REGISTRASTION).send_keys(
            AdditionalFunctions().generate_password())
        driver.find_element(*PageLocators.EMAIL_FIELD_REGISTRASTION).send_keys(AdditionalFunctions().generate_email())
        driver.find_element(*PageLocators.PWD_FIELD_REGISTRASTION).send_keys(
            AdditionalFunctions().generate_wrong_password())
        driver.find_element(*PageLocators.REGISTRATION_BUTTON_ON_REGISTR_PAGE).click()
        assert driver.find_element(*PageLocators.INCORRECT_PWD_TEXT).text == 'Некорректный пароль'
