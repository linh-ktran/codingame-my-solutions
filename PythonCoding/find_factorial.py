# 2) Factorial. Calculate a factorial of a number
#
# factorial(5) = 5! = 1 * 2 * 3 * 4 * 5 = 120
# factorial(10) = 10! = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8 * 9 * 10 = 3628800

def find_factorial(number: int) -> int:
    result = 1
    for i in range(2, number + 1):
        result *= i
    return result


# Using recursion
def factorial(n: int):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)


def main():
    for i in range(0, 11):
        print(f'{i}, {factorial(i)}')


main()
