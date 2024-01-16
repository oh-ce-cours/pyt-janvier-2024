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
        if num % 7 == 0:
            res += "Bazz"
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


def fizzbuzz4() -> None:
    for n in range(1, 101):
        print("fizz" * (n % 3 == 0) + "buzz" * (n % 5 == 0) or str(n))


fizzbuzz4()
