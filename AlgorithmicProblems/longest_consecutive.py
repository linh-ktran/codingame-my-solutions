# 128. Longest Consecutive Sequence
# Array, Hash Table, Union Find
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.
# You must write an algorithm that runs in O(n) time.
from typing import List


def longest_consecutive(nums):
    nums = sorted(nums)
    seen = set()
    no_duplicate = []
    for i in range(len(nums)):
        if nums[i] not in seen:
            seen.add(nums[i])
            no_duplicate.append(nums[i])

    if not no_duplicate:
        return 0

    current_total = 1
    global_total = 1
    for i in range(len(no_duplicate)-1):
        if no_duplicate[i] == no_duplicate[i+1] - 1:
            current_total += 1
            global_total = max(current_total, global_total)
        else:
            current_total = 1

    return global_total


#  Sorting || Iteration
def longest_consecutive_2(nums: List[int]) -> int:
    n = len(nums)
    if n == 0:
        return 0
    nums.sort()
    current_max = 1
    global_max = 0

    for i in range(1, n):
        if nums[i] != nums[i - 1]:
            if nums[i] == nums[i - 1] + 1:
                current_max += 1
                global_max = max(global_max, current_max)
            else:
                current_max = 1
    return max(global_max, current_max)


def main():
    nums = [100, 4, 200, 1, 3, 2]   #Output: 4
    #nums = []  # Output: 0
    #nums = [0, 1, 1, 2]
    result = longest_consecutive_2(nums)
    print(result)


main()
