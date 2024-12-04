def remove_duplicate_lines(source, destination):
    
    with open(source,'r' ,encoding='utf-8') as src:
        with open(destination,'w' ,encoding='utf-8') as dest:
            line = src.readline()
            last_line = ""
            while line != "":
                if line != last_line:
                    dest.write(line)
                    last_line = line
                
                line = src.readline()
            