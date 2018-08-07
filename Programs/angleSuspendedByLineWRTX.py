import math as m
"""
Typical Input
lx = (x0,x1,x2...) (0,5)
ly = (y0,y1,y2...) (0,0)
"""
def euclidianDistance(lx,ly):
    try:
        difxSqur = 0
        for i in range(len(lx)-1):
            difxSqur += (lx[i+1] - lx[i])**2
        difySqur = 0
        for i in range(len(ly)-1):
            difySqur += (ly[i+1] - ly[i])**2
        euclidDist = m.sqrt(difxSqur+difySqur)
        return euclidDist

    except Exception as e:
        print(e)
def angleSuspended(euclidDist,y0,yn):
    angle = m.asin((yn-y0)/euclidDist)
    return ((180/m.pi)*angle)%360
    
if __name__ == "__main__":
    try:
        lx = list(map(int,input().strip().split(sep = ",")))
        ly = list(map(int,input().strip().split(",")))
        d = euclidianDistance(lx,ly)
        print(d)
        print(angleSuspended(d,ly[0],ly[-1]),"degree",sep=" ")
    except Exception as e:
        print(e)
