# **1) FizzBuzz. Print numbers from 1 to 100
#
# - If it’s a multiplier of 3, print “Fizz”
# - If it’s a multiplier of 5, print “Buzz”
# - If both 3 and 5 — “Fizz Buzz"
# - Otherwise, print the number itself

def fizz_buzz(number: int) -> None:
    if number % 3 == 0 and number % 5 == 0:
        print("Fizz Buzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


def main():
    for i in range(0, 101):
        fizz_buzz(i)


main()
