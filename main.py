
from configparser import ConfigParser
from threading import Thread
from singleton import Singleton

parser = ConfigParser()
parser.read("config.properties")
# parser.read("sample_config.txt")
print(parser.get("config", "option2"))

def decorator(f):
    def funtionRet(*args, **kwargs):
        print("i am in the decorator")
        return f(*args, **kwargs)
    return funtionRet

@decorator
def add(a, b):
    return a + b

@decorator
def neg(n):
    return n * -1

def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)

process1 = Thread(target=test_singleton, args=("FOO",))
process2 = Thread(target=test_singleton, args=("BAR",))
process1.start()
process2.start()

