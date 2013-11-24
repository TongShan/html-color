#coding:utf-8

prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

sum = 0
for x in stock and prices:
    sum += (prices[x] * stock[x])
    print x
    print 'price: %s' % prices[x]
    print 'stock: %s' % stock[x]
    print 'sum: %s' % (prices[x] * stock[x])

print sum


