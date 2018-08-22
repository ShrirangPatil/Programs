#!/bin/python3
"""
INPUT 0:
Enter plain text:balloon
Enter k value	:3
Cipher Text	: edoorrq

INPUT 1:
Enter plain text:hi this is shrirang
Enter k value	:4
Cipher Text	: lm xlmw mw wlvmverk
"""
import sys
def unicodeToCharS(uni):
    num = uni
    for i in "abcdefghijklmnopqrstuvwxyz":
        if ord(i) == uni:
            return i
def unicodeToCharC(uni):
    num = uni
    for i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        if ord(i) == uni:
            return i
def caesarCipher(s, k):
    # Complete this function
    num = k
    result = ""
    while(num>26):
        num = num%26
    for i in range(len(s)):
        if ord(s[i]) >= 97 and ord(s[i]) <= 122:
            unicode = ord(s[i])+num
            if(unicode > 122):
                unicode = unicode%122
                unicode = 96+unicode
            result += unicodeToCharS(unicode)
        elif ord(s[i]) >= 65 and ord(s[i]) <= 90:
            unicode = ord(s[i])+num
            if(unicode > 90):
                unicode = unicode%90
                unicode = 64+unicode
            result += unicodeToCharC(unicode)
        else:
            result += s[i]
    return result

if __name__ == "__main__":
    s = input("Enter plain text:").strip()
    k = int(input("Enter k value\t:").strip())
    result = caesarCipher(s, k)
    print("Cipher Text\t:",result)
