import typing

type1 = typing.TypeVar("type1")
type2 = typing.TypeVar("type2")


def my_map(func: typing.Callable[[type1], type2], elements: list[type1]) -> list[type2]:
    res = []
    for element in elements:
        tmp = func(element)
        res.append(tmp)
    return res
