## Valid Pair Sum

Given an array of size N, find the number of distinct pairs {a[i], a[j]} (i != j) in the array with their sum greater than 0.

### Example 1:
Input: N = 3, a[] = {3, -2, 1}
Output: 2
Explanation: {3, -2}, {3, 1} are two possible pairs.

### Example 2:
Input: N = 4, a[] = {-1, -1, -1, 0}
Output: 0
Explanation: There are no possible pairs.

### Your Task: 
You don't need to read input or print anything.
Complete the function ValidPair() which takes the array a[ ] and size of array N as input parameters and returns the count of such pairs.

### Expected Time Complexity: O(N * Log(N))
### Expected Auxiliary Space: O(1)

### Constraints:
1 ≤ N ≤ 105

-104  ≤ a[i] ≤ 104
