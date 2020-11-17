from ip import *
from divider import *
from key import *
from split_plain import *
from f import *
from expant import *
from xor import *
from tablep import *
from inverse import *

plaintext = input("Input of Plaintext = ")
keytext = input("input of the key = ")

plain = ''.join(format(ord(i), 'b').zfill(8) for i in plaintext)  
key = ''.join(format(ord(j), 'b').zfill(8) for j in keytext) 

divider = divider(plain) #From file divide_block.py (split plaintext to a block-block 64bit)
length = len(divider)
result = []
ips = ['0']*2
pcs2 = ['0']*16
splitPlains = ['0']*16
list(splitPlains)
r_expands = ['0']*16
xors = ['0']*16
arrayDividers = ['0']*16
unionArrays = ['0']*16
binaryToDecimals = ['0']*16
f_functions = ['0']*16
decimalToBinarys = ['0']*16
addBits = ['0']*16
permutation = ['0']*16
result_xors = ['0']*16

for x in range(length):
    ips[x] = ip(divider[x])
    pcs2[x] = pc2(union(shift(split(pc1(key))))) #from file key.py
    splitPlains[x] = splitPlain(ips[x]) #from file split_plain.py (split 1 block of plaintext to be 32 bit left and right)
    for i in range(16): 
        r_expands[i] = expand(splitPlains[x][1]) #from file expant.py
        xors[i] = xor(r_expands[i], pcs2[x][i]) #xor r exapnded with key

        arrayDividers[i] = arrayDivider(xors[i])    #from file f.py
        unionArrays[i] = unionArray(arrayDividers[i])   #from file f.py
        binaryToDecimals[i] = binaryToDecimal(unionArrays[i])   #from file f.py
        f_functions[i] = f_function(binaryToDecimals[i], s) #from file f.py
        decimalToBinarys[i] = decimalToBinary(f_functions[i])   #from file f.py
        addBits[i] = addBit(decimalToBinarys[i])    #fromherd file f.py

        permutation[i] = permutasi(addBits[i]) #from file tablep.py
        result_xors[i] = xor(splitPlains[i][0], permutation[i]) #xor result from left block with permutation p
        splitPlains[i+1][0] = splitPlains[i][1]
        splitPlains[i+1][1] = result_xors[i]

    l_tmp = splitPlains[15][0]
    r_tmp = splitPlains[15][1]

    tmp = []
    for i in l_tmp:
        tmp.append(i)
    for  j in r_tmp:
        tmp.append(j)
    result.append(tmp)

    inverse = inverse(result)

for i in inverse:
    print(i)