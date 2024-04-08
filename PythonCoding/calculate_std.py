# 4) STD. Calculate the standard deviation of elements in a list.
#
# std([1, 2, 3, 4]) = 1.29
# std([1]) = NaN (use float('NaN'))
# std([]) = NaN

from math import sqrt
from statistics import mean


def calculate_std(numbers: list) -> float:
    if len(numbers) > 1:
        average = mean(numbers)
        total = sum((i - average)**2 for i in numbers)
        return sqrt(total/(len(numbers) - 1))
    return float("NaN")


def main():
    print(calculate_std([1, 2, 3, 4]))
    print(calculate_std([1]))
    print(calculate_std([]))


main()
