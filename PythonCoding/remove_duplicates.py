# 6) Remove duplicates. Remove duplicates in list. The list is not sorted and the order of elements from the original list should be preserved.
#
# [1, 2, 3, 1] ⇒ [1, 2, 3]
# [1, 3, 2, 1, 5, 3, 5, 1, 4] ⇒ [1, 3, 2, 5, 4]

def remove_duplicates(numbers: list) -> list:
    new_list = []
    for number in numbers:
        if number not in new_list:
            new_list.append(number)

    return new_list


def main():
    list1 = [1, 2, 3, 1]
    list2 = [1, 3, 2, 1, 5, 3, 5, 1, 4]
    print(remove_duplicates(list1))
    print(remove_duplicates(list2))


main()
