# 14) Three sum.
# Given an array, and a target value, find all possible combinations
# of three distinct numbers such that the sum of these three distinct numbers is equal to the target value.
#
# Example:
#
# Input: [12, 3, 1, 2, -6, 5, -8, 6], 0
# Output: [[-8, 2, 6], [-8, 3, 5], [-6, 1, 5]]

def three_sum(array: list, target: int):
    array = sorted(array)
    print(sorted(array))
    result = []
    for i in range(len(array) - 2):
        small_num = i+1
        big_num = len(array) - 1

        while small_num < big_num:
            sum = array[i] + array[small_num] + array[big_num]
            if sum == target:
                print(sum)
                result.append([array[i], array[small_num], array[big_num]])
                small_num += 1
                big_num -= 1
            elif sum > target:
                big_num -= 1
            elif sum < target:
                small_num += 1
    return result


def main():
    result = three_sum([12, 3, 1, 2, -6, 5, -8, 6], 0)
    print(result)


main()

