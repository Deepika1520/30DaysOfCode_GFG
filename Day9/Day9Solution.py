class Solution:
    def transfigure(self, a, b): 
        # code here 
        if len(a)!=len(b):
            return -1
         # dictionary taht will store the count of the lements present
        di={}
        #adding count of elements of a in dictionary
        for i in a :
            if i in di:
                di[i]+=1
            else:
                di[i]=1
        #decreasing the count if present in b striung else return -1 if alphabet not present
        for i in b:
            if i not in di:
                return -1
            else:
                di[i]-=1
                
        # checking that count of every alphabet is 0
        for i in di:
            if di[i]:
                return -1
         
        # the main logic tof find steps
        # i is pointer to a string and j is pointer to b string
        ans = 0
        i=j=len(a)-1
        while(i>=0):
            while(i>=0 and a[i]!=b[j]):
                ans+=1
                i-=1
            if(i>=0):
                i-=1
                j-=1
            
        
        return ans
