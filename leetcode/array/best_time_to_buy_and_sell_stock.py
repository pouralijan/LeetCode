def maxProfit(prices):
    """
    [7,1,5,3,6,4]
    """

    buy = prices[0]
    max_sell = 0
    for price in prices:
        sell = price - buy
        if sell > max_sell:
            max_sell = sell
        if price < buy:
            buy = price
    return max_sell


print(maxProfit([7,1,5,3,6,4]))

