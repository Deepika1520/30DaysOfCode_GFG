from collections import deque

dr = [-1, 0, 0, 1]
dc = [ 0,-1, 1, 0]

class Solution:
    def findDistance(self, matrix, m, n):
        ret = [ [-1 for _ in range(n)] for _ in range(m) ]
        q = deque()
    
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'B':
                    ret[i][j] = 0
                    q.append((i,j))
    
        while len(q):
            r=q[0][0]
            c=q[0][1]
            q.popleft()
    
            for i in range(4):
                nextr=r+dr[i]
                nextc=c+dc[i]
                if nextr>=0 and nextr<m and nextc>=0 and nextc<n:
                    if ret[nextr][nextc]==-1 and matrix[nextr][nextc]=='O':
                        ret[nextr][nextc] = ret[r][c]+1
                        q.append((nextr,nextc))
        return ret
