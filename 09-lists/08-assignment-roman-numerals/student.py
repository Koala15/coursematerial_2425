def  to_roman(n):
    num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

    roman = ''
    for (a , r) in num_map:
        while n >= a:
            roman += r
            n -= a
            if n == 0 :
                return roman

    return roman

def  from_roman(string):
    num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'), (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]

    num = 0
    i = 0
    while i < len(string):
        found = False
        if i + 1 < len(string):        # search a group of two chars
            s = string[i: i+2]
            for (a, r) in num_map:
                if s == r:          # found a group of two chars
                    num += int(a)
                    i += 2
                    found = True

        
        if not found:               # search a group of one char
            s = string[i]
            for (a, r) in num_map:
                if s == r:
                    num += int(a)
                    i +=1
   
    return num
