#coding:utf-8

prices = {"banana": 4, "apple": 2, "orange": 1.5, "pear": 3}
stock = {"banana": 6, "apple": 0, "orange": 32, "pear": 15}

shop_list = ['banana', 'orange', 'apple']

def compute_bill(food):
    total = 0
    for x in food:
        total += prices[x]
    return total

print compute_bill(shop_list)

