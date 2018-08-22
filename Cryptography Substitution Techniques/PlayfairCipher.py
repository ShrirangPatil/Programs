"""
The Playfair algorithm is based on the use of a 5 * 5 matrix of letters
constructed using a keyword.
KeyWord used is "MONARCHY"

Sample INPUT 0:
Enter the Plain Text:	"'hi this is shrirang...!'"
Formated plaintext:	 hithisisshrirang
Cipher generated:	 BFPDSXSXPBAKMRYQ
Plain text generated:	 hithisisshrirang

Sample INPUT 1:
Enter the Plain Text:	balloon
Formated plaintext:	 balxloon
Cipher generated:	 IBSUPMNA
Plain text generated:	 balxloon

Sample INPUT 2:
Enter the Plain Text:	xxx
Formated plaintext:	 xxxxxx
Cipher generated:	 ZZZZZZ
Plain text generated:	 xxxxxx
"""


table = [['M','O','N','A','R'],['C','H','Y','B','D'],['E','F','G','I','K'],
         ['L','P','Q','S','T'],['U','V','W','X','Z']]

def formatIt(plainText):
    x = 0
    temp = plainText[0:]
    for i in range(len(plainText)-1):
        if plainText[i] == plainText[i+1]:
            if (i+x)%2 == 0:
                temp = temp[0:i+1+x]+"x"+temp[i+1+x:]
                x +=1
    return temp

def encryption(plainText):
    index = 0
    cipherText = ""
    while(index < len(plainText)):
        one = plainText[index].upper()
        if one is "J":
            one = "I"
        oneij = []
        index += 1
        
        two = plainText[index].upper()
        if two is "J":
            two = "I"
        twoij = []
        index += 1
        
        for i in table:
            if one in i:
                oneij.append(table.index(i))
                oneij.append(i.index(one))

        for i in table:
            if two in i:
                twoij.append(table.index(i))
                twoij.append(i.index(two))
        #print(oneij,twoij,sep="\n")
        
        if oneij[0] == twoij[0]:
            row = oneij[0]
            onecol = (oneij[1]+1)%5
            twocol = (twoij[1]+1)%5
            cipherText += table[row][onecol]
            cipherText += table[row][twocol]
        elif oneij[1] == twoij[1]:
            col = oneij[1]
            onerow = (oneij[0]+1)%5
            tworow = (twoij[0]+1)%5
            cipherText += table[onerow][col]
            cipherText += table[tworow][col]
        else:
            onerow = oneij[0]
            onecol = twoij[1]
            tworow = twoij[0]
            twocol = oneij[1]
            cipherText += table[onerow][onecol]
            cipherText += table[tworow][twocol]
    return cipherText

def decryption(cipherText):
    index = 0
    plainText = ""
    while(index < len(cipherText)):
        one = cipherText[index]
        oneij = []
        index += 1
        
        two = cipherText[index]
        twoij = []
        index += 1
        #print(one,two,index)
        for i in table:
            if one in i:
                oneij.append(table.index(i))
                oneij.append(i.index(one))

        for i in table:
            if two in i:
                twoij.append(table.index(i))
                twoij.append(i.index(two))
        #print(oneij,twoij,sep="\n")
        
        if oneij[0] == twoij[0]:
            row = oneij[0]
            onecol = (oneij[1]-1)%5
            twocol = (twoij[1]-1)%5
            plainText += table[row][onecol]
            plainText += table[row][twocol]
        elif oneij[1] == twoij[1]:
            col = oneij[1]
            onerow = (oneij[0]-1)%5
            tworow = (twoij[0]-1)%5
            plainText += table[onerow][col]
            plainText += table[tworow][col]
        else:
            onerow = oneij[0]
            onecol = twoij[1]
            tworow = twoij[0]
            twocol = oneij[1]
            plainText += table[onerow][onecol]
            plainText += table[tworow][twocol]
    return plainText
if __name__ == "__main__":
    plainText = input("Enter the Plain Text:\t")
    for i in ''' ;:,.!-'"_=''':
        plainText = plainText.replace(i,"")
    plainText = formatIt(plainText)
    if len(plainText)%2 != 0:
        plainText += "x"
    print("Formated plaintext:\t",plainText)
    cipherText = encryption(plainText)
    print("Cipher generated:\t",cipherText)
    plainText = decryption(cipherText)
    print("Plain text generated:\t",plainText.lower())
            
            
