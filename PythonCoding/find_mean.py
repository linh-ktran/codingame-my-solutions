# 3) Mean. Compute the mean of number in a list
#
# mean([4, 36, 45, 50, 75]) = 42
# mean([]) = NaN (use float('NaN'))

def find_mean(numbers: list) -> float:
    if len(numbers) > 0:
        return sum(numbers)/len(numbers)
    return float("NaN")


def main():
    print(find_mean([4, 36, 45, 50, 75]))
    print(find_mean([]))


main()
