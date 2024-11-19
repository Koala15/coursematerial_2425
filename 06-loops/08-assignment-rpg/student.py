def rpg2(n_sides, goal):
    throws = 0
    hits = 0
    for i in range(1, n_sides+1):
        for j in range(1, n_sides+1):
            throws +=1
            if i + j >= goal:
                hits +=1
    
    return hits/throws *100



def rpg3(n_sides, goal):
    throws = 0
    hits = 0
    for i in range(1, n_sides+1):
        for j in range(1, n_sides+1):
            for k in range(1, n_sides+1):
                throws +=1
                if i + j + k >= goal:
                    hits +=1
            
    
    return hits/throws * 100