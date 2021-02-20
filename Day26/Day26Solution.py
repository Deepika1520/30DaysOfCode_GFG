from collections import defaultdict

class Solution:
    def checkCycle(self, i):
        global isstack
        global visited
        global counted
        global ve
        if (isstack[i] == 1):
            return rue
        # insert into stack
        isstack[i] = 1
        for it in ve[i]:
            # if next node is visited
            if (visited[it] == 1):
                # if the node is in stack then cycle is found
                if (isstack[it] == 1):
                    return True
                continue
            visited[it] = 1
            if (self.checkCycle(it)==True):
                return True;
        # removing from stack   
        isstack[i] = 0
        return False
    
    def dfs(self, i, duration):
        global counted
        global visited
        global isstack
        global ve
        #  return the time to complete the project starting from the node i if it is
        #  already calculated
        if (counted[i] != -1):
            return counted[i]
        x = 0;
    
        for it in ve[i]:
            x = max(x, self.dfs(it, duration))
        #  time to complete this module and maximum time to complete child modules
        counted[i] = x + duration[i]
        return counted[i]
    
    def minTime(self, vp, duration, n, m):
        independent=[0]*(n+5)
        global ve
        ve = defaultdict(lambda:[])
        for i in range(0,m):
            x = vp[i][0]
            y = vp[i][1]
            ve[x].append(y)
            independent[y]+=1
        global visited
        global counted
        global isstack
        visited =[-1]*(n+5)
        counted =[-1]*(n+5)
        isstack =[-1]*(n+5)
        
        flag = 0;
        for i in range(0,n):
            if (independent[i] == 0):
                flag = 1
        # no independent module
        if (flag == 0):
            return -1
    
        for i in range(0,n):
            if (independent[i] != 0):
                continue
            visited[i] = 1
            # checking cycle 
            if (self.checkCycle(i)):
                return -1
        
        ans = 0;
        # starting from any independent module find the maximum time to complete
        # the project
        for i in range(0,n):
            if (independent[i] == 0):
                ans = max(ans, self.dfs(i, duration));
    
        return ans;
