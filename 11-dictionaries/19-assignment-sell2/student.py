def sell2(stock, model, size):
    
    stock_model = stock.get(model, dict())
    found = False

    if len(stock_model):                    # model found
        stock_model_size = stock[model].get(size, 0)    #size found
    
        if stock_model_size:
            stock[model][size] = stock_model_size -1
            found = True
            if(stock[model][size] == 0):
                del stock[model][size]
            if(len(stock[model]) == 0):
                del stock[model]
    
 
    return found