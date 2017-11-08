import numpy as np
import time
import timeit
import math

lsb = True
msb = False

#num & -num  return least sig digits
def lsb_1(num):
    return((num & -num).bit_length()-1)
    #time = 62.42
    #correct

def lsb_2(num):
    return(math.log2(num & -num))
    #time = 82.45
    #correct

def lsb_3(num):
    shifts = 0
    while(num%2==0):
        num = num >> 1
        shifts += 1
    return(shifts)
    #time = 83.89
    #correct

# def lsb_4(num): #DOESNT WORK
#   return(num & 1)

# def lsb_5(num): #DOESNT WORK
#   return(num % 2)

def get_lsb_board(board):
    return(num & -num)

def get_msb_board(board):
    return(2**msb_4)

def msb_1(num):
    shifts = 0
    while(num != 1):
        num = num >> 1
        shifts += 1
    return(shifts)
    #time = 372.04
    #correct

# def msb_2(num):
#   #Wrong
#   count = 0
#   while(num):
#       num = num&(num-1)
#       count += 1
#   return(count)

def msb_3(num):
    count = 0
    while(num != 1):
        num = num//2
        count += 1
    return(count)
    #time = 403
    #correct 

def msb_4(num):
    num = np.uint64(num)
    num2 = num.byteswap()
    print(np.binary_repr(num,width=64), ':', num)
    print(np.binary_repr(num2,width=64), ":", num2)
    return(64-int((num2 & -num2)).bit_length()-1)

def msb_5(num):
    return(num.bit_length()-1)
    #time = 46.972
    #correct 

if lsb:
    print("lsb 1")
    print(timeit.timeit('for n in range(1,100000): lsb_1(n)', setup="from __main__ import lsb_1",number = 1000))
    print("\n")

    print("lsb 2")
    print(timeit.timeit('for n in range(1,100000): lsb_2(n)', setup="from __main__ import lsb_2",number = 1000))
    print("\n")

    print("lsb 3")
    print(timeit.timeit('for n in range(1,100000): lsb_3(n)', setup="from __main__ import lsb_3",number = 1000))
    print("\n")

    # print("lsb 4")
    # print(timeit.timeit('for n in range(1,100000): lsb_4(n)', setup="from __main__ import lsb_4",number = 1000))
    # print("\n")

    # print("lsb 5")
    # print(timeit.timeit('for n in range(1,100000): lsb_5(n)', setup="from __main__ import lsb_5",number = 1000))
    # print("\n")

    m1 = []
    m2 = []
    m3 = []
    # m4 = []
    # m5 = []
    for i in range(1,1000):
        m1.append(lsb_1(i))
        m2.append(lsb_2(i))
        m3.append(lsb_3(i))
        # m4.append(lsb_4(i))
        # m5.append(lsb_5(i))

    assert(m1 == m2)
    assert(m2 == m3)

if msb:
    print("msb 1")
    print(timeit.timeit('for n in range(1,100000): msb_1(n)', setup="from __main__ import msb_1",number = 1000))
    print("\n")

    # print("msb 2")
    # print(timeit.timeit('for n in range(1,100000): msb_2(n)', setup="from __main__ import msb_2",number = 1000))
    # print("\n")

    print("msb 3")
    print(timeit.timeit('for n in range(1,100000): msb_3(n)', setup="from __main__ import msb_3",number = 1000))
    print("\n")

    # print("msb 4")
    # print(timeit.timeit('for n in range(1,100000): msb_4(n)', setup="from __main__ import msb_4",number = 1000))
    # print("\n")

    print("msb 5")
    print(timeit.timeit('for n in range(1,100000): msb_5(n)', setup="from __main__ import msb_5",number = 1000))
    print("\n")

    m1 = []
    m2 = []
    m3 = []
    m4 = []
    m5 = []

    for i in range(1,1000):
        m1.append(msb_1(i))
        # m2.append(msb_2(i))
        m3.append(msb_3(i))
        # m4.append(msb_4(i))
        m5.append(msb_5(i))
    # assert(m1 == m2)
    # assert(m2 == m3)
    # print(m1)
    # print(m4)
    # print(m5)
    assert(m1 == m3)
    # assert(m1 == m4)
    assert(m1 == m5)
    # assert(m3 == m4)