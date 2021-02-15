## Corona Vaccine
Geek has developed an effective vaccine for Corona virus and he wants each of the N houses in Geek Land to have access to it.
Given a binary tree where each node represents a house in Geek Land, find the minimum number of houses that should be supplied with the vaccine kit if one vaccine kit is sufficient for that house, its parent house and it's immediate child nodes.  

### Example 1:
Input:

    1
    
  /   \
  
 2      3
      
          \
          
             4
             
                \
                
                  5
                  
                    \
                    
                       6
  
Output: 2

Explanation: The vaccine kits should be supplied to house numbers 1 and 5. 

### Example 2:
Input:

    1
    
  /   \
  
 2      3
  
Output: 1

Explanation: The vaccine kits should be supplied to house number 1.

### Your Task:
You don't need to read input or print anything. Complete the function supplyVaccine() which takes the root of the housing tree as input parameter and returns the minimum number of houses that should be supplied with the vaccine kit.

### Expected Time Complexity: O(N)
### Expected Auxiliary Space: O(N)

### Constraints:
1 ≤ N ≤ 105

### Topic: Tree

### Hint

Use Greedy approach to take care of the following types of cases
1. Node is a leaf node
2. Node is already covered by another node
3. Node itself has the vaccine kit
