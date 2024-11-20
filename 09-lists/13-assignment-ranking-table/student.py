def  ranking_table(ranking):
    l_name = max(len(name) for name, timing in ranking)
    l_ranking = len(str(len(ranking)))
    index = 1
    lines =""
    for name, timing in ranking:
        lines += str(index).rjust(l_ranking) + " " + name.ljust(l_name) + " " + f"{timing:.2f}"
        if index < len(ranking):
            lines += "\n"
        index +=1
    return lines