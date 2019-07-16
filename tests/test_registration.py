from tests.browser import Driver
from pages.registration_page import RegisterAccountPage, RegistrationSuccessPage
from tests.person import Director, ConcreteBuilder
from enum import Enum


class Field(Enum):
    NAME = 0
    LAST_NAME = 1
    EMAIL = 2
    PHONE = 3
    PASSWORD = 4


def test_registration() -> None:
    chrome = Driver().connect()
    director = Director()
    builder = ConcreteBuilder()
    director.builder = builder
    director.build_registration()
    registration = RegisterAccountPage()
    registration.open()
    person = str(builder.person.list_parts()).split(',')
    print(person)
    registration.fill_personal_details(person[Field.NAME.value],
                                       person[Field.LAST_NAME.value],
                                       person[Field.EMAIL.value],
                                       person[Field.PHONE.value],
                                       person[Field.PASSWORD.value]
                                       )
    registration.press_continue()
    assert RegistrationSuccessPage(chrome).loaded()
