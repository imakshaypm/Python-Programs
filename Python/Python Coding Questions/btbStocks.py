def bestTime(prices):
    x = list(prices)
    x.sort()
    buyprice = x[0]
    if buyprice in prices:
        buyday = prices.index(buyprice)
    sellday = buyday
    for i in range(sellday + 1, len(prices)):
        if prices[i] >= prices[sellday]:
            sellday = i
    if sellday == buyday:
        return 0
    else:
        return prices[sellday] - prices[buyday]

l = [1, 2]
print(bestTime(l))