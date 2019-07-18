import copy
from mimesis import Person

from tests.person import Director, ConcreteBuilder

generator = Person()


class Prototype:

    def __init__(self):
        self._toBeClonedObjects = {}

    def registerObject(self, name, obj):
        self._toBeClonedObjects[name] = obj

    def unregisterObject(self, name):
        del self._toBeClonedObjects[name]

    def clone(self, name, **kwargs):
        clonedObject = copy.deepcopy(self._toBeClonedObjects.get(name))
        clonedObject.__dict__.update(kwargs)
        return clonedObject


def prot():
    defaultCar = ConcreteBuilder()
    prototype = Prototype()
    prototype.registerObject('persons_data', defaultCar)
    persons_data = prototype.clone('persons_data', firstname=generator.name(), surname=generator.last_name(),
                                   email=generator.email(), phone=generator.telephone(),
                                   password=generator.password())
    return persons_data


def build_prot():
    director = Director()
    builder = prot()
    director.builder = builder
    return director.builder
