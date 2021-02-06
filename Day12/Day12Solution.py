def sumBitDiff(self, arr, n): 
        # Your code goes here
        ans = 0  
        for i in range(0, 32): 
            count = 0
            for j in range(0, n): 
                if ( (arr[j] & (1 << i)) ): 
                    count+= 1
            ans += (count * (n - count) * 2); 
      
        return ans
