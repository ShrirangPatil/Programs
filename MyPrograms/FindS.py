"""
FindS without inductive bias

"""
noOfTrainEx = 4#int(input("Enter the no of training examples"))
noOfAttri = 7#int(input("Enter the no of attributes"))
trainEx = [["Sunny","Warm","Normal","Strong","Warm","Same","Yes"],
           ["Sunny","Warm","High","Strong","Warm","Same","Yes"],
           ["Sunny","Cold","High","Strong","Warm","Same","No"],
           ["Sunny","Warm","High","Strong","Cool","Change","Yes"]]
ex = []
#print(trainEx)
hypo = [0,0,0,0,0,0,0]
for i in trainEx:
    if i[6] == "Yes":
        for j in range(len(i)):
            if i[j] != hypo[j] and hypo[j] == 0:
                hypo[j] = i[j]
            elif i[j] == hypo[j]:
                pass
            else:
                hypo[j] = "?"
            print(hypo[0:6])
print(hypo[0:6])
"""
sample output
['Sunny', 0, 0, 0, 0, 0]
['Sunny', 'Warm', 0, 0, 0, 0]
['Sunny', 'Warm', 'Normal', 0, 0, 0]
['Sunny', 'Warm', 'Normal', 'Strong', 0, 0]
['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 0]
['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same']
['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same']
['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same']
['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same']
['Sunny', 'Warm', '?', 'Strong', 'Warm', 'Same']
['Sunny', 'Warm', '?', 'Strong', 'Warm', 'Same']
['Sunny', 'Warm', '?', 'Strong', 'Warm', 'Same']
['Sunny', 'Warm', '?', 'Strong', 'Warm', 'Same']
['Sunny', 'Warm', '?', 'Strong', 'Warm', 'Same']
['Sunny', 'Warm', '?', 'Strong', 'Warm', 'Same']
['Sunny', 'Warm', '?', 'Strong', 'Warm', 'Same']
['Sunny', 'Warm', '?', 'Strong', 'Warm', 'Same']
['Sunny', 'Warm', '?', 'Strong', 'Warm', 'Same']
['Sunny', 'Warm', '?', 'Strong', '?', 'Same']
['Sunny', 'Warm', '?', 'Strong', '?', '?']
['Sunny', 'Warm', '?', 'Strong', '?', '?']
['Sunny', 'Warm', '?', 'Strong', '?', '?']
"""
