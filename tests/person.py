from abc import ABC, abstractmethod, abstractproperty
from typing import Any
import copy
from mimesis import Person


class Builder(ABC):
    @abstractproperty
    def person(self) -> None:
        pass

    @abstractmethod
    def person_name(self) -> None:
        pass

    @abstractmethod
    def person_surname(self) -> None:
        pass

    @abstractmethod
    def person_email(self) -> None:
        pass

    @abstractmethod
    def person_phone(self) -> None:
        pass

    @abstractmethod
    def person_password(self) -> None:
        pass


class Person():
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def list_parts(self) -> None:
        return ', '.join(self.parts)


class ConcreteBuilder(Builder):

    def __init__(self) -> None:
        self.firstname = 'Alex'
        self.surname = 'First'
        self.email = 'alexfirst1@gmail.com'
        self.phone = '+3809900001'
        self.password = 'Qwertyui212'
        self.reset()

    def reset(self) -> None:
        self._person = Person()

    @property
    def person(self) -> Person:
        person = self._person
        self.reset()
        return person

    def person_name(self) -> None:
        self._person.add(self.firstname)

    def person_surname(self) -> None:
        self._person.add(self.surname)

    def person_email(self) -> None:
        self._person.add(self.email)

    def person_phone(self) -> None:
        self._person.add(self.phone)

    def person_password(self) -> None:
        self._person.add(self.password)


class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> Builder:
        return self._builder

    @builder.setter
    def builder(self, builder: Builder) -> None:
        self._builder = builder

    def build_registration(self) -> None:
        self.builder.person_name()
        self.builder.person_surname()
        self.builder.person_email()
        self.builder.person_phone()
        self.builder.person_password()

    def build_login(self) -> None:
        self.builder.person_email()
        self.builder.person_password()


def build():
    director = Director()
    builder = ConcreteBuilder()
    director.builder = builder
    return director.builder
