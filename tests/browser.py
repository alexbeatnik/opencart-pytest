from selenium import webdriver


class MetaClassSingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaClassSingleton, cls).__call__(
                *args, **kwargs
            )

        return cls._instances[cls]


class Driver(metaclass=MetaClassSingleton):
    connection = None

    def connect(self):
        if self.connection is None:
            self.connection = webdriver.Chrome("/Users/opol2/Downloads/chromedriver")

        return self.connection

    def close_connection(self):
        if self.connection is not None:
            self.connection.close()
            return self.connection
