# prices = [7, 1, 5, 3, 6, 4]
# [2,9,1,5]
def max_profit(prices):
    buy_p = prices[0]
    profit = 0
    for i in range(1, len(prices)):
        if buy_p > prices[i]:
            buy_p = prices[i]
        elif prices[i] - buy_p > profit:
            profit = prices[i] - buy_p
    return profit


gained_max_profit = max_profit([7, 1, 5, 3, 6, 4])
print(gained_max_profit)
