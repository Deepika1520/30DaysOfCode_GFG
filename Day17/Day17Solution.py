#GFG's Solution
from collections import deque

class Solution:
    def help_classmate(self, arr, n):
        stack = deque()
        ret = [-1 for _ in range(n)]
        
        for i in range(n):
            while len(stack) and arr[i] < arr[stack[-1]] :
                ret[ stack.pop() ] = arr[i]
            stack.append(i)
        
        return ret
        
        
# My Soltuion
def help_classmate(self, arr, n):
        # Your code goes here
        # Return the list
        k2=[];
        for i in range(n):
            k1=arr[i];
            z=i+1;
            while z<n: 
                if k1>arr[z]:
                    k2.append(arr[z]);
                    break;
                z=z+1;
            else:
                k2.append(-1);
        return k2;
