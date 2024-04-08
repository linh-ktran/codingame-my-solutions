# 1. Two Sum
# Array, Hash Table
#
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.


# Brute force
def two_sum_1(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    n = len(nums)
    for i in range(n-1):
        for j in range(1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []  # No solution found


# Two-pass Hash Table
def two_sum_2(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    n = len(nums)

    # Build the hash table:
    hash_table = {nums[i]: i for i in range(n)}

    for i in range(n):
        delta = target - nums[i]
        if delta in nums and hash_table[delta] != i:
            return [i, hash_table[delta]]
    return []


# One-pass Hash Table
def two_sum_3(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    n = len(nums)

    # Build the hash table:
    hash_table = {}

    for i in range(n):
        delta = target - nums[i]
        if delta in hash_table:
            return [hash_table[delta], i]
        hash_table[nums[i]] = i
    return []


def main():
    nums = [2, 7, 11, 15]
    target = 9
    nums = [3, 2, 4]
    target = 6
    print(two_sum_3(nums, target))


main()
