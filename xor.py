def xor(i,j):
    result = []
    length = len(i)
    for x in range(length):
        if i[x] == "0" and j[x] == "1":
            result.append(1)
        elif i[x] == "1" and j[x] == "0":
            result.append(1)
        else:
            result.append(0)
    return result