from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from constants import Constants
from constants import Urls
from locators import Locators


class TestPersonalAccountNavigation:
#Переход с главной страницы в ЛК
    def test_navigation_main_page_to_personal_account_successful(self, driver):
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

        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(Locators.HEADER_ACCOUNT_PROFILE))
        assert driver.current_url == Urls.PROFILE_FORM_URL
#Переход из ЛК к конструктору
    def test_navigation_personal_account_to_constructor_by_link_successful(self, driver):
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
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.BUTTON_ORDER))

        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(Locators.HEADER_ACCOUNT_PROFILE))
        assert driver.current_url == Urls.PROFILE_FORM_URL

        driver.find_element(*Locators.MENU_CONSTRUCTOR).click()
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(Locators.BUTTON_ORDER))

        assert driver.current_url == Urls.HOME_PAGE_URL
class TestConstructorNavigation:
  #Переход к конструктору - булки
    def test_navigation_constructor_to_buns(self, driver):
        WebDriverWait(driver, 3).until(EC.visibility_of_element_located(Locators.ORDER_HEADER))

        driver.find_element(*Locators.BUTTON_FILLINGS).click()
        assert driver.find_element(*Locators.HEADER_FILLINGS).is_displayed()

        driver.find_element(*Locators.BUTTON_BUNS).click()
        assert driver.find_element(*Locators.HEADER_BUNS).is_displayed()
        
#Переход к конструктору - соусы
    def test_navigation_constructor_to_sauces(self, driver):
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.ORDER_HEADER))

        driver.find_element(*Locators.BUTTON_SAUCES).click()
        assert driver.find_element(*Locators.HEADER_SAUCES).is_displayed()
#Переход к конструктору-начинки
    def test_navigation_constructor_to_fillings(self, driver):
        WebDriverWait(driver, 3).until(
            EC.visibility_of_element_located(Locators.ORDER_HEADER))

        driver.find_element(*Locators.BUTTON_FILLINGS).click()
        assert driver.find_element(*Locators.HEADER_FILLINGS).is_displayed()
#Разлогин из ЛК
    def test_exit_from_personal_account_successful(self, driver):
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

        driver.find_element(*Locators.PERSONAL_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(Locators.HEADER_ACCOUNT_PROFILE))
        assert driver.current_url == Urls.PROFILE_FORM_URL

        driver.find_element(*Locators.BUTTON_EXIT_ACCOUNT).click()
        WebDriverWait(driver, 3).until(
            EC.presence_of_element_located(Locators.ENTRANCE_HEADER))
        assert driver.current_url == Urls.LOGIN_FORM_URL
