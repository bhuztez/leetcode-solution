def maxProfit(prices):
    if not prices:
        return 0

    l = len(prices)

    profit = [[0 for _ in prices] for _ in range(2) ]
    cost = [[0 for _ in prices] for _ in range(2) ]

    cost[0][0] = -prices[0]
    cost[1][0] = -prices[0]

    for i in range(1, l):
        cost[0][i] = max(-prices[i], cost[0][i-1])
        profit[0][i] = max(profit[0][i-1], prices[i] + cost[0][i-1])

    for i in range(1, l):
        cost[1][i] = max(profit[0][i-1]-prices[i], cost[1][i-1])
        profit[1][i] = max(profit[1][i-1], prices[i] + cost[1][i-1])

    return profit[-1][-1]
