def ip(plain):
    tmp = []
    i = 57
    for _ in range(32):
        if i>=0:
            tmp.append(plain[i])
            i = i-8
        else:
            i = i + 66
            tmp.append(plain[i])

    i = 56
    for _ in range(32):
        if i>=0:
            tmp.append(plain[i])
            i = i-8
        else:
            i = i + 66
            tmp.append(plain[i])

    return tmp
