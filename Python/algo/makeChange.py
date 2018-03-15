import math

def change(cents):
    coins = {}
    coins['dollars'] = math.floor(cents/100)
    cents-=100*coins['dollars']
    coins['quarter'] = math.floor(cents/25)
    cents-=25*coins['quarter']
    coins['dime'] = math.floor(cents/10)
    cents-=10*coins['dime']
    coins['nickel'] = math.floor(cents/5)
    cents-=5*coins['nickel']
    coins['penny'] = math.floor(cents/1)
    cents-=1*coins['penny']
    print(cents)
    print(coins)
    return coins

change(469)
    

