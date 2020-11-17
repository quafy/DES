def splitPlain(plain):
    left = []
    right = []
    i = 0 

    for x in plain: #loop for split a key in 2 pieces (C0 and D0)
        if i < 28:
            left.append(x)
            i = i+1
        else:
            right.append(x)
            i = i+1

    return left, right