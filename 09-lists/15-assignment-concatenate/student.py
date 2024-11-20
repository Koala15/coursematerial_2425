def concatenate(xs, ys):
    #print ( "xs is " + str(xs) + " and ys is " + str(ys))
    
    if (xs is ys):
        count = len(ys)
        for i in range(0,count):
            xs.append(ys[i])
    else:
        for y in ys:
            xs.append(y)

    #print ( "xs is " + str(xs) )
