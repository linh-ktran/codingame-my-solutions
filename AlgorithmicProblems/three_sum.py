# 14) Three sum.
# Array, Two Pointers, Sorting
# Given an array, and a target value, find all possible combinations
# of three distinct numbers such that the sum of these three distinct numbers is equal to the target value.
#
# Input: [12, 3, 1, 2, -6, 5, -8, 6], 0
# Output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

def three_sum(array: list, target: int):
    array = sorted(array)
    result = []
    for i in range(len(array) - 2):
        small_num = i+1
        big_num = len(array) - 1

        while small_num < big_num:
            sum = array[i] + array[small_num] + array[big_num]
            if sum == target:
                three = [array[i], array[small_num], array[big_num]]
                if three not in result:
                    result.append(three)
                small_num += 1
                big_num -= 1
            elif sum > target:
                big_num -= 1
            elif sum < target:
                small_num += 1
    return result


def three_sum_2(array: list, target: int):
    array.sort()
    s = set()
    n = len(array)
    for i in range(n):
        j = i + 1
        k = n - 1
        while j < k:
            sum = array[i] + array[j] + array[k]
            if sum == target:
                s.add((array[i], array[j], array[k]))
                j += 1
                k -= 1
            elif sum > target:
                k -= 1
            else:
                j += 1
    result = list(s)
    return result


def main():
    result = three_sum([12, 3, 1, 2, -6, 5, -8, 6], 0)
    result = three_sum([-1, 0, 1, 2, -1, -4], 0)
    print(result)


main()

