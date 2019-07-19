from modules.proxy import Proxy, RealSubject


def test_registration() -> None:
    assert Proxy(RealSubject()).request()
