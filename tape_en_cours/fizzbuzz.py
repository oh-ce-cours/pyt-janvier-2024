def fizzbuzz1():
    for num in range(1, 101):
        res = None
        if not num % 3 and not num % 5:
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


def fizzbuzz3() -> None:
    for number in range(1, 101):
        match number % 3, number % 5:
            case 0, 0:
                print("fizzbuzz")
            case _, 0:
                print("buzz")
            case 0, _:
                print("fizz")
            case _:
                print(number)


fizzbuzz2()
