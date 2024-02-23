
def sum_by_letter(input_arr: list) -> str:
    """
    Function to get the sum by key letters.

    Parameters:
    input_arr: List of items.

    Returns:
    (str) Sum by letters.

    """
    # Create a dict with the letter sums
    letter_sums = {}
    for item in input_arr:
        letter, value = item.split(":")
        letter_sums[letter] = letter_sums.get(letter, 0) + int(value)

    # Filter letter_sums 0
    filter_dict = {key: value for key, value in letter_sums.items() if value != 0}

    # Sort the keys alphabet
    # sorted_dict = dict(sorted(filter_dict.items()))
    sorted_letters = sorted(filter_dict.keys())

    # Generate the desired format for the output.
    list_sums = [f"{letter}:{filter_dict[letter]}" for letter in sorted_letters]

    result = ",".join(list_sums)
    return result


def main():
    arr = ["X:-1", "Y:1", "X:-4", "B:3", "X:5"]     # Output: B:3,Y:1
    # arr = ["Z:0", "A:-1"]                         # Output: A:-1
    # arr = ["B:-1", "A:1", "B:3", "A:5"]           # Output:"A:6,B:2"
    result = sum_by_letter(arr)
    print(result)
    return result


main()
