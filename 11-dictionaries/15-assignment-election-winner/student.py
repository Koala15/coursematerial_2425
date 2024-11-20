def election_winner(votes):
    #winner = ""
    
    list_votes = list(votes)
    #print (list_votes)
    if len(list_votes):
        results = dict()
        for name in list_votes:
            count = results.get(name,0) + 1
            results[name] = count
        
        max_count = max(results.values())
        #print ("max_count is " + str(max_count))
        for name, count in results.items():
            if count == max_count:
                return name

    return None