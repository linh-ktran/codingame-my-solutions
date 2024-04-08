# 11) RLE. Implement RLE (run-length encoding): encode each character by the number of times it appears consecutively.
#
# 'aaaabbbcca' ⇒ [('a', 4), ('b', 3), ('c', 2), ('a', 1)]
# (note that there are two groups of 'a')

import itertools


def rle(group):
    return [(l, len(list(g))) for l, g in itertools.groupby(group)]


def run_length_encoding(group: str):
    result = []
    value_ref = group[0]
    freq = 0
    for i in range(len(group)):
        if group[i] == value_ref:
            freq += 1
        else:
            result.append((value_ref, freq))
            value_ref = group[i]
            freq = 1
        if i == len(group) - 1:
            result.append((value_ref, freq))
    return result


def main():
    print(run_length_encoding('aaaabbbcca'))
    print(rle('aaaabbbcca'))


main()
