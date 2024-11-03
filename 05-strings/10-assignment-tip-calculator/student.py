# write your code here
def tip_calculator():
    total_price = int(input("total price: "))
    tip = input("tip percentage (default=20): ")

    if tip == '':
        tip = 20
    else:
        tip = int(tip)
        
    tip = int(total_price  * tip / 100)
    
    total_price = total_price + tip
    print (f"You have to pay {total_price}")