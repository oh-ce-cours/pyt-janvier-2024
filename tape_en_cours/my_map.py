import typing

# on est obligé de définir des types génériques
type1 = typing.TypeVar("type1")
type2 = typing.TypeVar("type2")


def my_map(func: typing.Callable[[type1], type2], elements: list[type1]) -> list[type2]:
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