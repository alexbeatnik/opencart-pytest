from selenium.webdriver import Remote
from pages.base import Page
from modules.browser import Driver

driver = Driver().connect()


class PersonalDetails:
    def __init__(self):
        self._browser = driver

    def type_first_name(self, first_name: str) -> None:
        self._browser.find_element_by_id("input-firstname").send_keys(first_name)

    def type_last_name(self, last_name: str) -> None:
        self._browser.find_element_by_id("input-lastname").send_keys(last_name)

    def type_email(self, email: str) -> None:
        self._browser.find_element_by_id("input-email").send_keys(email)

    def type_telephone(self, telephone: str) -> None:
        self._browser.find_element_by_id("input-telephone").send_keys(telephone)

    def type_password(self, password: str) -> None:
        self._browser.find_element_by_id("input-password").send_keys(password)

    def confirm_password(self, password: str) -> None:
        self._browser.find_element_by_id("input-confirm").send_keys(password)


class RegisterAccountPage(Page):
    def __init__(self):
        self._browser = driver
        self._details = PersonalDetails()

    def open(self) -> None:
        self._browser.get(f"https://127.0.0.1/index.php?route=account/register")

    def loaded(self) -> bool:
        return "Register Account" in self._browser.title

    def fill_personal_details(
        self, first_name: str, last_name: str, email: str, telephone: str, password: str
    ) -> None:
        self._details.type_first_name(first_name)
        self._details.type_last_name(last_name)
        self._details.type_email(email)
        self._details.type_telephone(telephone)
        self._details.type_password(password)
        self._details.confirm_password(password)

    def press_continue(self) -> None:
        self._browser.find_element_by_name("agree").click()
        self._browser.find_element_by_xpath('//input[@value="Continue"]').click()


class RegistrationSuccessPage(Page):
    def __init__(self, browser: Remote) -> None:
        self._browser = browser

    def open(self) -> None:
        raise RuntimeError("This page can't be open through an URL")

    def loaded(self) -> bool:
        return "success" in self._browser.current_url
