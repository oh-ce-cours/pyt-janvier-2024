import sys


def test2():
    try:
        return 1 + "1"
    except IndexError:
        return "exception"


print(test2())
