# Maximum Sum Contiguous Subarray. You are given an array A of length N, you have to find the largest possible sum of an Subarray, of array A.
#
# [-2, 1, -3, 4, -1, 2, 1, -5, 4] gives 6 as largest sum (from the subarray [4, -1, 2, 1]

def max_sum_subarray(array):
    current_max = array[0]
    global_max = array[0]
    for i in range(1, len(array)):
        current_max = max(array[i], current_max + array[i])
        global_max = max(current_max, global_max)
    return global_max


def main():
    array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(max_sum_subarray(array))


main()
