from faker import Faker


class AbstractFactory(object):
    def create_name(self):
        pass

    def create_last_name(self):
        pass


class Name(object):
    def __init__(self, name):

        self._name = name

    def __str__(self):
        return self._name


class Contacts(object):
    def __init__(self, name):

        self._name = name

    def __str__(self):
        return self._name


class ConcreteFactory1(AbstractFactory):
    def create_name(self):
        return Name(Faker().first_name())

    def create_last_name(self):
        return Contacts(Faker().last_name())


class ConcreteFactory2(AbstractFactory):
    def create_name(self):
        return Name(Faker("uk_UA").first_name())

    def create_last_name(self):
        return Contacts(Faker("uk_UA").last_name())


def get_factory(ident):
    if ident == 'Latin':
        return ConcreteFactory1()

    elif ident == 'Cyrillic':
        return ConcreteFactory2()


def full_person(fabric):
    factory = get_factory(fabric)
    return (
        str(factory.create_name())+','
        + str(factory.create_last_name()) + ','
        + f"{Faker().ascii_free_email()},{Faker().phone_number()},{Faker().password(special_chars=False)}"
    )
# print(full_person(2))