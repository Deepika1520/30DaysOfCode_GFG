
def repeatedStringMatch(self, a, b):
    strlen = int(len(b) / len(a))+2
    count=1
    StrA=a
    for i in range(strlen+1):
        if(b in a): 
            return count
        else:
            a+=StrA
            count+=1
    return -1; 
