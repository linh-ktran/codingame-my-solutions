# 121. Best Time to Buy and Sell Stock
# Array, Dynamic Programming, Sliding Window
#
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future
# to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


def max_profit(prices):
    """
    :type prices: List[int]
    :rtype: int
    """
    buy = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        if prices[i] - buy < 0:
            buy = prices[i]
        elif prices[i] - buy > profit:
            profit = prices[i] - buy
    return profit


def main():
    prices = [7, 6, 4, 3, 1]     # Output: 0
    prices = [7, 1, 5, 3, 6, 4]  # Output: 5
    prices = [2, 4, 1]           # Output: 2
    prices = [1]                 # Output: 2
    prices = [3, 2, 6, 5, 0, 3]
    print(max_profit(prices))


main()
