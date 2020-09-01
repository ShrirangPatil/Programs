import math

def primeOrNot(num):
    for i in range(2,int(math.sqrt(num))+1):
        if num%i == 0:
            return False
    return True

def primeGen():
    i = 2
    while True:
        if primeOrNot(i):
            yield i
        i = i + 1

def Prime(num):
    lis = []
    for i in primeGen():
        if not num:
            break
        lis.append(i)
        num -= 1
    return lis

for i in primeGen():
    print(i)
