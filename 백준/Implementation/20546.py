def buy(stock_cnt, stock_price, m):
    if stock_price <= m:  # 남은 돈보다 주가가 같거나 작으면, 살 수 있는만큼 구매
        stock_cnt += (m // stock_price)
        m %= stock_price
    return stock_cnt, m


def sell(stock_cnt, stock_price, m):
    if stock_cnt > 0:
        m += stock_cnt * stock_price
        stock_cnt = 0
    return stock_cnt, m


def jun(m):
    stock_cnt = 0
    for price in data:
        stock_cnt, m = buy(stock_cnt, price, m)
    return m + stock_cnt * data[-1]


def sung(m):
    stock_cnt = 0
    inc, dec = 0, 0
    for i in range(1, 14):
        if data[i - 1] < data[i]:
            dec = 0
            inc += 1
            if inc >= 3:
                stock_cnt, m = sell(stock_cnt, data[i], m)

        if data[i - 1] > data[i]:
            inc = 0
            dec += 1
            if dec >= 3:
                stock_cnt, m = buy(stock_cnt, data[i], m)

    return m + stock_cnt * data[-1]


import sys
input = sys.stdin.readline

money = int(input())
data = list(map(int, input().split()))

j, s = jun(money), sung(money)
if j > s:
    print("BNP")
elif j < s:
    print("TIMING")
else:
    print("SAMESAME")
