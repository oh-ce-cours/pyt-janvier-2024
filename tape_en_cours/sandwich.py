# On veut print des chesseburgers

# pain
# salade
# fromage
# tomate
# steak
# salade
# pain


def pain(f):
    def wrapper():
        res = f()
        return res

    return wrapper


def salade(f):
    def wrapper():
        res = f()
        return res

    return wrapper


def fromage(f):
    def wrapper():
        res = f()
        return res

    return wrapper


def tomate(f):
    def wrapper():
        res = f()
        return res

    return wrapper


@pain
@salade
@fromage
@tomate
def viande():
    print("steak")


viande()