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


def salade():
    print("salade")


@pain
@salade
@ingredient("fromage")
def viande():
    print("steak")


viande()
