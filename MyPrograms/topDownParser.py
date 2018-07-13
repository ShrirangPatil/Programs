"""
Grammar
E -> Te
e -> +Te | epi                       where e = E', t = T' and epicilon = "" 
T -> Ft
t -> *Ft | epi
F -> (E) | d
"""
"""
sample input
(d+d)*d
(((((((d)))))))+(d)+(d*d)
(d+d+d+d)*(d*d*) # Invalid expression
"""
parsingTable = {'E':{"d":"Te","(":"Te"},
                "e":{"+":"+Te",")":"","$":""},
                "T":{"d":"Ft","(":"Ft"},
                "t":{"+":"","*":"*Ft",")":"","$":""},
                "F":{"d":"d","(":"(E)"}}

def parser(string):
    stack = "E$"
    flag = 0
    action = ""
    print("Stack","Input","Action",sep="  ")
    while(True):
        print(stack,string,action,sep="\t")
        if stack[0] == "$" and string[0] == "$":
            print("Valid String")
            break
        elif stack[0] == string[0]:
            action = "match "+stack[0]
            print(action)
            stack = stack[1:]
            string = string[1:]
        else:
            if string[0] in parsingTable[stack[0]].keys():
                action = parsingTable[stack[0]].get(string[0])
                stack = parsingTable[stack[0]].get(string[0]) + stack[1:]
            else:
                print("Invalid String")
                break
if __name__ == "__main__":
    string = input("Enter a string: ")
    string = string+"$"
    parser(string)
    
