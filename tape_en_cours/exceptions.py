import sys


def test2():
    try:
        return 1 + "1"
    except:
        return "exception"
    finally:
        print("dans finally", sys.exc_info())
        return "finally"


print(test2())
