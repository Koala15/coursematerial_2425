def cake(stock, recipe_ingredients):
    counts = set()    
    for ingredient, quantity in recipe_ingredients.items():
        stock_i = stock.get(ingredient, 0)
        n_cakes = 0
        if stock_i > 0:
            n_cakes = int(stock_i / quantity)
        counts.add(n_cakes)

    return min(counts)