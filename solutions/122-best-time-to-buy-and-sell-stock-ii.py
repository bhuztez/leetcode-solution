from iterator import izip

def maxProfit(prices):
    profit = 0

    for previous, current in izip(prices[:-1],prices[1:]):
        if current > previous:
            profit += current - previous
                
    return profit
