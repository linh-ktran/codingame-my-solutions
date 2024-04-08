# 217. Contains Duplicate
# Array, Hash Table, Sorting
#
# Given an integer array nums,
# return true if any value appears at least twice in the array,
# and return false if every element is distinct.

# Brute force
def contains_duplicate_1(nums) -> bool:
    """
    :type nums: List[int]
    :rtype: bool
    """
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] == nums[j]:
                return True
    return False


# Sorting Approach
def contains_duplicate_2(nums) -> bool:
    """
    :type nums: List[int]
    :rtype: bool
    """
    nums.sort()
    n = len(nums)
    for i in range(n-1):
        if nums[i] == nums[i+1]:
            return True
    return False


def contains_duplicate_3(nums) -> bool:
    """
    :type nums: List[int]
    :rtype: bool
    """
    # Hash table approach
    seen = set()
    for i in range(len(nums)):
        if nums[i] in seen:
            return True
        seen.add(nums[i])
    return False


def main():
    nums1 = [1, 2, 3, 1]  # True
    nums2 = [1, 2, 3, 4]  # False
    nums3 = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]  # True
    result = contains_duplicate_3(nums3)
    print(result)


main()
