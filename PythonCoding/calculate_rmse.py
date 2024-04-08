# 5) RMSE. Calculate the RMSE (root mean squared error) of a model.
# The function takes in two lists: one with actual values, one with predictions.
#
# rmse([1, 2], [1, 2]) = 0
# rmse([1, 2, 3], [3, 2, 1]) = 1.63

from math import sqrt


def calculate_rmse(numbers: list, predictions: list) -> float:
    assert len(numbers) == len(predictions), 'different sizes of the arguments'

    return sqrt(
        sum((numbers[i]-predictions[i])**2 for i in range(len(numbers)))/len(numbers)
    )


def main():
    print(calculate_rmse([1, 2], [1, 2]))
    print(calculate_rmse([1, 2, 3], [3, 2, 1]))


main()
