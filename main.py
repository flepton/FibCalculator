def fib(number_fib):
    if number_fib < 2:
        return number_fib
    else:
        return fib(number_fib-1) + fib(number_fib-2)

def main():
    number_fib = int(input("Plz write number Fibonacci: "))
    print(fib(number_fib))


if __name__ == "__main__":
    main()