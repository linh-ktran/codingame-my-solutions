# 482. License Key Formatting
# You are given a license key represented as a string s that consists of only alphanumeric characters and dashes. The string is separated into n + 1 groups by n dashes. You are also given an integer k.
# We want to reformat the string s such that each group contains exactly k characters, except for the first group, which could be shorter than k but still must contain at least one character. Furthermore, there must be a dash inserted between two groups, and you should convert all lowercase letters to uppercase.
# Return the reformatted license key.


def license_key_formatting(s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    new_s = [val for val in s if val != '-']
    new_s.reverse()
    result = []
    index = [i for i in range(len(new_s)) if not i % k]
    for i in index:
        letters = new_s[slice(i, i+k)]
        letters.reverse()
        result.append(''.join(letters))
    result.reverse()
    return '-'.join(result).upper()


def license_key_formatting_2(s, k):
    """
    :type s: str
    :type k: int
    :rtype: str
    """
    # Eliminate all dashes
    s = s.replace('-', '')
    remander = len(s) % k
    grouping = []
    if remander:
        grouping.append(s[:remander])

    for i in range(remander, len(s), k):
        grouping.append(s[i:i+k])

    return '-'.join(grouping).upper()


def main():
    s = "5F3Z-2e-9-w-2-5g3-Jc"
    k = 4
    result = license_key_formatting_2(s, k)
    print(result)


main()
