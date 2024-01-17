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
        print("pain")
        res = f()
        print("pain")
        return res

    return wrapper


def salade(f):
    def wrapper():
        print("salade")
        res = f()
        print("salade")
        return res

    return wrapper


def fromage(f):
    def wrapper():
        print("fromage")
        res = f()
        return res

    return wrapper


def tomate(f):
    def wrapper():
        res = f()
        print("tomate")
        return res

    return wrapper


def ingredient(nom_ingredient, lower=False, upper=False):
    def factory_ingredient(f):
        def wrapper():
            if upper:
                print(nom_ingredient)
            res = f()
            if lower:
                print(nom_ingredient)
            return res

        return wrapper

    return factory_ingredient


@ingredient("pain", upper=True, lower=True)
@ingredient("salade", upper=True, lower=True)
@ingredient("tomate", lower=True)
@ingredient("fromage", upper=True)
def viande():
    print("steak")


# viande = pain(salade(viande))

# viande = (ingredient("pain", True, True))(viande)

viande()
