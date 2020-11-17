def divider(a):
    b = len(a) #total bit
    e = int(b%64)
    i = []
    p = []
    
    if e != 0:
        for _ in range(64-e): #repetition to fill the rest
            a = a + "0"
    
    for y in a:
        i.append(y)
        if len(i) >= 64:
            p.append(i)
            i = []

    return p