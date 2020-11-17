import collections
def pc1(key):
    tmp = []
    tmp1 = []
    for i in key:
        tmp.append(i)
    tpc1 = [
    56, 48, 40, 32, 24, 16, 8, 0, 57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18, 10, 2, 59, 51, 43, 35, 62, 54, 46, 38, 30, 22, 14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 60, 52, 44, 36, 28, 20, 12, 4, 27, 19, 11, 3]
    for i in tpc1:
        tmp1.append(tmp[i])
    return tmp1

def split(key):
    left = []
    right = []
    i = 0 

    for x in key: #loop for split a key in 2 pieces (C0 and D0)
        if i < 28:
            left.append(x)
            i = i+1
        else:
            right.append(x)
            i = i+1

    # print("Left :")
    # for x in left:
    #     print(x)

    # print("Right :")
    # for x in right:
    #     print(x)

    return left, right

def shift(split):
    shift = [1,1,2,2,2,2,2,2,1,2,2,2,2,2,2,1]
    tmp_left = []
    tmp_right = []
    left_result = []
    right_result = []

    tmp_left = collections.deque(split[0])
    for i in shift:
        tmp_left.rotate(i)
        left_shifted = list(tmp_left)
        left_result.append(left_shifted)

    tmp_right = collections.deque(split[1])
    for i in shift:
        tmp_right.rotate(i)
        right_shifted = list(tmp_right)
        right_result.append(right_shifted)

    return left_result, right_result

def union(shift): #Join each left and right key after shift (C0 with D0, C1 with D1, ...)
    tmp = []
    result = []
    for x in range(16):
        for y in shift[0][x]:
            tmp.append(y)
        for z in shift[1][x]:
            tmp.append(z)
        result.append(tmp)
        tmp = []
    return result

def pc2(union): #Do PC2 due to table PC2
    table_pc2 = [14,17,11,24,1,5,3,28,15,6,21,10,23,19,12,4,26,8,16,7,27,20,13,2,41,52,31,37,47,55,30,40,51,45,33,48,44,49,39,56,34,53,46,42,50,36,29,32]
    result = []
    tmp = []
    for x in range(16):
        for y in table_pc2:
            tmp.append(union[x][y-1])
        result.append(tmp)
        tmp = []
    return result