# brute force method

# def stock_prices(stocks):
#     n = len(stocks)
#     max_profit = 0
#     for i in range(n - 1):
#         for j in range(i + 1, n - 1):
#             profit = stocks[j] - stocks[i]
#             if profit > max_profit:
#                 max_profit = profit
#             else:
#                 max_profit = max_profit
#     return max_profit

# brute force method

def stock_prices(stocks):
    n = len(stocks)
    max_profit = 0
    # set initial minimum price to a very large value
    min_price = float('inf')
    for i in range(n):
        # get minimum price between 2 stocks
        min_price = min(min_price, stocks[i])
        # get max profit between 2 stocks
        max_profit = max(max_profit, stocks[i] - min_price)

    return max_profit


print(stock_prices([10, 7, 5, 8, 11, 9]))
