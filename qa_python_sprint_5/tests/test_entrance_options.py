from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from locators import Locators


class TestLogin:
#Вход с правильными кредами через ЛК
    def test_login_via_personal_area_valid_cred_successful(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.ENTRANCE_HEADER))

        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(
            Constants.USER_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(
            Constants.PASSWORD)

        driver.find_element(*Locators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(
            EC.invisibility_of_element(Locators.ENTRANCE_HEADER))

        assert driver.find_element(*Locators.BUTTON_ORDER).is_displayed()

#Вход через кнопку аккаунт с валидиными кредами
    def test_login_via_enter_account_valid_cred_successful(self, driver):
        enter_account_btn = driver.find_element(*Locators.BUTTON_ENTER_ACCOUNT)
        driver.execute_script("arguments[0].scrollIntoView();", enter_account_btn)
        enter_account_btn.click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.ENTRANCE_HEADER))

        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(
            Constants.USER_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(
            Constants.PASSWORD)

        driver.find_element(*Locators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(
            EC.invisibility_of_element(Locators.ENTRANCE_HEADER))

        assert driver.find_element(*Locators.BUTTON__ORDER).is_displayed()

#Проверка логина через форму регистрации с валидными кредами
    def test_login_via_registration_form_valid_cred_successful(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.ENTRANCE_HEADER))

        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(
            Constants.USER_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(
            Constants.PASSWORD)

        driver.find_element(*Locators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(
            EC.invisibility_of_element(Locators.ENTRANCE_HEADER))

        assert driver.find_element(*Locators.BUTTON_ORDER).is_displayed()

#Вход через форму "Забыли пароль" с валидными кредами
    def test_login_via_forgot_password_valid_cred_successful(self, driver):
        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.ENTRANCE_HEADER))

        driver.find_element(*Locators.BUTTON_RESTORE_PASSWORD).click()
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.HEADER_RESTORE_PASSWORD))

        driver.find_element(*Locators.BUTTON_ENTER_ACCOUNT_FROM_RESTORE_FORM).click()

        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.ENTRANCE_HEADER))

        driver.find_element(*Locators.EMAIL_INPUT_FIELD).send_keys(
            Constants.USER_EMAIL)
        driver.find_element(*Locators.PASSWORD_INPUT_FIELD).send_keys(
            Constants.PASSWORD)

        driver.find_element(*Locators.BUTTON_ENTER).click()
        WebDriverWait(driver, 3).until(
            EC.invisibility_of_element(Locators.ENTRANCE_HEADER))

        assert driver.find_element(*Locators.BUTTON_ORDER).is_displayed()
