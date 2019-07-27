# RG
# 5a.6 #todo v.imp for interview especially stock1 and stock_sir as they are optimized


# def stock(_list):
#     n = len(_list)
#     profit = 0
#     buy = 0
#     sell = 0
#     for i in range(n):
#         for j in range(i):
#             if _list[i] - _list[j] > profit:
#                 profit = _list[i] - _list[j]
#                 buy = j
#                 sell = i
#         profit = _list[buy] - _list[sell]
#     return _list[buy], _list[sell]


def stock1(_list):
    n = len(_list)
    buy = 0
    sell = 0
    profit = 0
    for i in range(n):                                                  # todo 2 conditions not required
        if _list[buy] > _list[i] and profit > _list[buy] - _list[sell]:
            buy = i
        if _list[sell] < _list[i] and i > buy:
            sell = i
        profit = _list[buy] - _list[sell]
    return _list[buy], _list[sell]


def stock_sir(stock):
    min = stock[0]
    max = 0
    purchase = stock[0]
    sell = stock[0]
    for i in range(len(stock)):
        v = stock[i]
        if v-min > max:
            max = v-min
            purchase = min
            sell = v
        if v < min:
            min = v
    return max, purchase, sell


print(stock1([2, 4, 6, 8, 1, 2]))
print(stock_sir([2, 4, 6, 8, 1, 2]))


