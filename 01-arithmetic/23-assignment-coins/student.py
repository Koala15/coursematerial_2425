# write your code here
import math

def coins(amount):
    coin_5 = amount // 5
    amount = amount - (coin_5 * 5)
    coin_2 = amount // 2
    coin_1 = amount - (coin_2 * 2)

    return coin_5 + coin_2 + coin_1
    