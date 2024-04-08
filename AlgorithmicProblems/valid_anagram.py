# 242. Valid Anagram
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.

from collections import defaultdict


# Sorting
# Time complexity: O(n log n)
def valid_anagram_1(s: str, t: str) -> bool:
    print(sorted(s))
    print(sorted(t))
    return sorted(s) == sorted(t)


# Hash Table
# Time complexity: O(n)
def valid_anagram_2(s: str, t: str) -> bool:
    count_table = defaultdict(int)
    print(count_table)
    for letter in s:
        count_table[letter] += 1
    for letter in t:
        count_table[letter] -= 1
    for val in count_table.values():
        if val != 0:
            return False
    return True


# Hash Table (Using Array)
# Time complexity: O(n)
def valid_anagram_3(s: str, t: str) -> bool:
    count_array = [0]*26  # 26 letters
    for letter in s:
        count_array[ord(letter) - ord('a')] += 1

    for letter in t:
        count_array[ord(letter) - ord('a')] -= 1

    # Check if any character has non-zero frequency
    for val in count_array:
        if val != 0:
            return False
    return True


def main():
    s = "anagram"
    t = "nagaram"
    # True
    s = "rat"
    t = "car"
    # False
    result = valid_anagram_3(s, t)
    print(result)


main()
