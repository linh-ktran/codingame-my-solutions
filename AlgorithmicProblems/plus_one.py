
def plus_one(digits):
    """
    :type digits: List[int]
    :rtype: List[int]
    """
    first_night = None

    if digits[len(digits) - 1] == 9:
        first_night = len(digits) - 1
        for i in reversed(range(len(digits) - 1)):
            if digits[i] == 9 and digits[i] == digits[i + 1]:
                first_night = i

    if first_night == 0:
        for i in range(1, len(digits)):
            digits[i] = 0
        digits.append(0)
        digits[0] = 1

    elif first_night is None:
        digits[len(digits)-1] = digits[len(digits)-1] + 1
    else:
        digits[first_night-1] = digits[first_night-1] + 1
        for i in range(first_night, len(digits)):
            digits[i] = 0

    print(first_night)
    print(digits)


def plus_one2(digits):
    for i in range(len(digits)-1, -1, -1):
        print(i)
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] = digits[i] + 1
            return digits
    return [1] + digits


def main():
    digits = [1, 2, 3, 9, 9, 9]
    #digits = [4, 9, 9, 0, 0, 9]
    #digits = [7, 2, 8, 5, 0, 9, 1, 2,9,5,3,6,6,7,3,2,8,4,3,7,9,5,7,7,4,7,4,9,4,7,0,1,1,1,7, 4, 0, 0, 9]
    #digits = [1, 2, 3, 4]
    plus_one2(digits)
    print(plus_one2(digits))


main()
