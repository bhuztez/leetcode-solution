def maxProfit(prices):
    if len(prices) < 2:
        return 0

    low = min(prices[0], prices[1])
    pro = max(prices[1]-prices[0], 0)

    for p in prices[2:]:
        if p < low:
            low = p
        if p - low > pro:
            pro = p - low

    return pro
