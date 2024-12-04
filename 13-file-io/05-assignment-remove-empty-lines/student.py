def remove_empty_lines(source, destination):
    
    with open(source,'r' ,encoding='utf-8') as src:
        with open(destination,'w' ,encoding='utf-8') as dest:
            line = src.readline()
            while line != "":
                if line != "\n":
                    dest.write(line)
                
                line = src.readline()
            