"""Suppose we could access yesterday's stock prices as a list, where: The
indices are the time in minutes past trade opening time, which was 9:30am
local time.
The values are the price in dollars of Apple stock at that time.
So if the stock cost $500 at 10:30am, stock_prices_yesterday[60] = 500.
Write an efficient function that takes stock_prices_yesterday and returns the
best profit I could have made from 1 purchase and 1 sale of 1 Apple stock
yesterday."""


def find_profits(xs):
    """Return list of lists [sell price, purchase price, profit.]"""
    mn = 0       # min - purchase price
    profit = 0   # max- sell price
    result = []

    for i in range(len(xs) - 1):
        mx = max(xs[i + 1:])

        if xs[i] < mn or mn == 0:
            mn = xs[i]
            profit = mx - mn
            result.append([mx, mn, profit])
    return result

def find_best_profit(xs):
    return max(find_profits(xs), key=lambda row: row[2])


if __name__ == '__main__':

    # list of prices
    xs = [10, 9, 11, 7, 8, 30, 20, 5, 8, 22 , 11, 25, 9]
    print find_best_profit(xs)

    assert find_best_profit(xs) == [30, 7, 23]

