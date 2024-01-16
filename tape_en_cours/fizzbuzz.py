def fizzbuzz1():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


def fizzbuzz2():
    for num in range(1, 101):
        res: str = ""
        if num % 3 == 0:
            res += "Fizz"
        if num % 5 == 0:
            res += "Buzz"
        if not res:
            res = num
        print(res)
