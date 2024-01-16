3 % 2 == 0


for nombre in range(1, 101):
    if nombre > 10 and nombre % 2 == 0:
        print(nombre)
    elif nombre > 20:
        print("plus grand", nombre)
    else:
        print("plus petit", nombre)


print("fizz" or 2)
