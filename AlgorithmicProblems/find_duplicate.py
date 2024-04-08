# 15) Find Duplicate in array Given and array, find all duplicated value in the array
#
# Example:
#
# input: [1,2,3,4,3,4,5] output: [3,4]

def find_duplicate(array: list) -> list:
    seen = []
    seen1 = set()
    duplicate = []
    for i in range(len(array)):
        if array[i] not in seen:
            seen.append(array[i])
            seen1.add(array[i])
            print(seen1)
        else:
            duplicate.append(array[i])

    return duplicate


def main():
    input_array = [1, 2, 3, 4, 3, 4, 5]
    print(find_duplicate(input_array))


main()
