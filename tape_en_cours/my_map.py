import typing

# on est obligé de définir des types génériques
type1 = typing.TypeVar("type1")
type2 = typing.TypeVar("type2")


def my_map(func: typing.Callable[[type1], type2], elements: list[type1]) -> list[type2]:
    """reimplémentation de map

    Args:
        func (typing.Callable[[type1], type2]): la fonction a appliquer
        elements (list[type1]): la liste d'éléments sur laquelle appliquer la fonction

    Returns:
        list[type2]: la liste où on a appliqué la fonction sur chaque élément
    """
    res = []
    for element in elements:
        tmp = func(element)
        res.append(tmp)
    return res


def f(x: int) -> str:
    return str(x)


def f2(x: str) -> int:
    return int(x)


def f3(x: int) -> int:
    return x


a = my_map(f, [1, 2, 3])
b = my_map(f3, [1, 2])

help(my_map)
