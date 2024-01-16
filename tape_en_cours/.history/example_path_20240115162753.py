import pathlib

p = pathlib.Path(".")
p2 = p / ".."
print(p2.resolve().absolute())
print([f for f in p2.glob("**/*") if f.is_file()])

2 + 2


def f(a: int) -> int:
    return a + 1
