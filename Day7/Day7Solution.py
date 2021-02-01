 class Solution:
    def ValidPair(self, a, n): 
        a.sort()
        front=0
        tail=n-1
        ans=0
        while(front<tail): 
            if (a[front]+a[tail])>0:
                ans+=(tail-front)
                tail-=1
            else:
                front+=1
        return ans

if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        array=list(map(int,input().strip().split())
        obj = Solution()
        ans = obj.ValidPair(array, n)
        print(ans)
        
