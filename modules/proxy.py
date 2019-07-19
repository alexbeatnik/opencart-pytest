from abc import ABC, abstractmethod
from enum import Enum
from pages.registration_page import RegisterAccountPage, RegistrationSuccessPage
from modules.person import Director, ConcreteBuilder
from modules.browser import Driver


def number():
    try:
        with open("numfile.txt", "r") as numfile:
            for number in numfile:
                return number
    except FileNotFoundError:
        pass


class Field(Enum):
    NAME = 0
    LAST_NAME = 1
    EMAIL = 2
    PHONE = 3
    PASSWORD = 4


class Subject(ABC):
    @abstractmethod
    def request(self) -> None:
        pass


class RealSubject(Subject):
    def request(self) -> bool:
        chrome = Driver().connect()
        director = Director()
        builder = ConcreteBuilder()
        director.builder = builder
        director.build_registration()
        registration = RegisterAccountPage()
        registration.open()
        person = str(builder.person.list_parts()).split(",")
        registration.fill_personal_details(
            person[Field.NAME.value],
            person[Field.LAST_NAME.value],
            person[Field.EMAIL.value] + number(),
            person[Field.PHONE.value],
            person[Field.PASSWORD.value],
        )
        registration.press_continue()
        return RegistrationSuccessPage(chrome).loaded()


class Proxy(Subject):
    save_number = 1

    def __init__(self, real_subject: RealSubject) -> None:
        self._real_subject = real_subject
        self.save_number = "1"

    def request(self) -> None:
        if self.check_access():
            if self._real_subject.request():
                self.log_access()
                return True

    def check_access(self) -> bool:
        print("Proxy: Checking access prior to firing a real request.")
        try:
            with open("numfile.txt", "r") as numfile:
                for number in numfile:
                    if int(number):
                        self.save_number = int(number) + 1
                        return True

        except FileNotFoundError:
            with open("numfile.txt", "w") as numfile:
                numfile.write("1")
                self.save_number = "2"
                return True

    def log_access(self) -> None:
        with open("numfile.txt", "w") as numfile:
            numfile.write(str(self.save_number))
        Driver().close_connection()
