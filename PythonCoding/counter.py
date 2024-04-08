# 7) Count. Count how many times each element in a list occurs.
#
# [1, 3, 2, 1, 5, 3, 5, 1, 4] ⇒
#
# 1: 3 times
# 2: 1 time
# 3: 2 times
# 4: 1 time
# 5: 2 times

from collections import Counter


def my_counter(numbers: list) -> dict:
    result = {key: 0 for key in numbers}
    for number in numbers:
        result[number] += 1
    return result


def my_counter2(numbers: list) -> dict:
    counter = dict()
    for number in numbers:
        counter[number] = counter.get(number, 0) + 1
    return counter


def main():
    numbers = [1, 3, 2, 1, 5, 3, 5, 1, 4]
    result1 = Counter(numbers)
    result2 = my_counter2(numbers)
    print(result1)
    print(result2)


main()
