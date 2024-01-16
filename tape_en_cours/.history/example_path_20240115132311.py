import pathlib

p = pathlib.Path(".")
p2 = p / ".."
print(p2.resolve().absolute())
