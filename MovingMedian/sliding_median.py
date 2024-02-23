def get_median(input_list: list) -> float | int:
    """
    Function to get the median of a list of numbers.

    Parameters:
    input_list: List of numbers.

    Returns:
    (float, int) Median of the list.

    """
    n = len(input_list)
    sorted_list = sorted(input_list)
    # Division and rounds down to the nearest integer.
    mid = n // 2

    if n % 2 != 0:
        # For odd-length list, return the middle element of the list
        return sorted_list[mid]
    else:
        # For even-length list, an average the middle two elements
        return (sorted_list[mid - 1] + sorted_list[mid]) / 2


def get_moving_medians(input_list: list, window_size: int) -> str:
    """
    Function to get the moving medians of a list of numbers.

    Parameters:
    input_list: List of numbers.
    window_size: Size of sliding window.

    Returns:
    (str) Moving median.
    """
    moving_medians = []

    # For the first few elements (until the window size is reached)
    for i in range(window_size - 1):
        current_window = input_list[0:i+1]
        median = get_median(current_window)
        moving_medians.append(round(median))
        print(current_window)

    # When the window size is reached
    for i in range(len(input_list) - window_size + 1):
        current_window = input_list[i:i+window_size]
        median = get_median(current_window)
        moving_medians.append(round(median))
        print(current_window)

    results = ','.join(map(str, moving_medians))
    return results


def main():
    #arr = [3, 1, 3, 5, 10, 6, 4, 3, 1]
    #arr = [5, 2, 4, 6]
    arr = [3, 0, 0, -2, 0, 2, 0, -2]
    result = get_moving_medians(
        input_list=arr[1:],
        window_size=arr[0]
    )
    print(result)
    return result


main()
