def fizzbuzz1():
    for num in range(1, 101):
        res = None
        if num % 3 == 0 and num % 5 == 0:
            res = "FizzBuzz"
        elif num % 3 == 0:
            res = "Fizz"
        elif num % 5 == 0:
            res = "Buzz"
        else:
            res = str(num)
        print(res)


def fizzbuzz2() -> None:
    for num in range(1, 101):
        res = ""
        if num % 3 == 0:
            res += "Fizz"
        if num % 5 == 0:
            res += "Buzz"
        if not res:
            res = str(num)
        print(res)


fizzbuzz2()
