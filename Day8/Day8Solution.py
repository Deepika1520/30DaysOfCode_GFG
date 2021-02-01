class Solution:
    def maxCandy(self, height, n): 
        # Your code goes here
        ans=0
        start=0
        end=n-1
        
        while(start<end):
            length=end-start-1
            minvalue=min(height[start],height[end])
            area=length*minvalue
            ans=max(ans,area)
            if height[start] < height[end]:
                start+=1
            else:
                end-=1
        return ans
  
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        n = int(input())
        array=list(map(int,input().strip().split())
        obj = Solution()
        ans = obj.maxCandy(array, n)
        print(ans)
