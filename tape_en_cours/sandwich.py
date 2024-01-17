# On veut print des chesseburgers

# pain
# salade
# fromage
# tomate
# steak
# salade
# pain


def pain():
    print("pain")


def salade():
    print("salade")


@pain
@salade
def viande():
    print("steak")


viande()
