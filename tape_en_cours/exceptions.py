def test2():
    try:
        return 1 + "1"
    except IndexError:
        return "exception"
    finally:
        return "finally"


print(test2())
