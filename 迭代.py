def findMinAndMax(L):
    Min = L[0]
    Max = L[0]
    for i in L:
        if Min > i:
            Min = i
        if Max < i:
            Max = i
        else: pass
    return Min, Max
    
        
