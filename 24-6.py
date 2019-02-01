prices = list(map(int, input().split(';')))
prices.sort(reverse=True)
for price in prices:
    print('{:>9,d}'.format(price))