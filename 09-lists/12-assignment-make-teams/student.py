def make_teams(participants, team_size):
    teams = []
    participants_count = len(participants)

    if participants_count <= team_size:
        teams.append(participants)
    else:
        nr_teams = int(len(participants) / team_size)
        #rest = len(participants) % team_size
        next_p = nr_teams * team_size      # the index of the first extra player
    
        #print("participants " + str(len(participants)) + " nr_teams " + str(nr_teams) + " of team_size " + str(team_size) + " and rest " + str(rest) + " next_p " + str(next_p))
    
        for i in range (0, nr_teams):
            new_team = []
            if ((i+1) * team_size < participants_count):
                new_team = participants[i * team_size: (i+1) * team_size]
            else:
                new_team = participants[i * team_size: participants_count]
            teams.append(new_team)
        
        #print (teams)
        while next_p < participants_count:
            for i in range (0, nr_teams):
                if next_p < participants_count:
                    teams[i].append(participants[next_p])
                    next_p += 1
       
    #print (teams)
    return teams