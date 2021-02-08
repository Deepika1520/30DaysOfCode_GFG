def digitSum(self, n): 
    	sum = 0
    	while (n): 
    		sum += (n % 10) 
    		n //= 10
    	return sum
	
def RulingPair(self, arr, n): 
  mp = dict() 
  ans = -1
  for i in range(n):  
    dSum = self.digitSum(arr[i]) 

    if (dSum in mp): 
      ans = max(ans, mp[dSum] + arr[i]) 
    mp[dSum] = max(mp.get(dSum, 0) ,arr[i]) 
  return ans 
