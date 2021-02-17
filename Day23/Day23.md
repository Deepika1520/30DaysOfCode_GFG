## Lucy's Neighbours
Lucy lives in house number X. She has a list of N house numbers in the society. Distance between houses can be determined by studying the difference between house numbers. Help her find out K closest neighbors.
Note: If two houses are equidistant and Lucy has to pick only one, the house with the smaller house number is given preference.

### Example 1:
Input:

N = 5, X = 0, K = 4

a[] = {-21, 21, 4, -12, 20}, 

Output:-21 -12 4 20

Explanation: The closest neighbour is housenumber 4. Followed by -12 and 20. -21 and 21 are both equal distance from X=0.
Therefore, Lucy can only pick 1. Based on the given condition she picks -21 as it is the smaller of the two. 

### Example 2:
Input:N = 6, X = 5, K = 3 

a[] = {10, 2, 14, 4, 7, 6},

Output:4 6 7 

### Your Task: 
You don't need to read input or print anything.
Complete the function  Kclosest() which takes the array arr[], size of array N, X, and K as input parameters, and returns the list of numbers in sorted order.

### Expected Time Complexity: O(NlogN)
### Expected Auxiliary Space: O(N)

### Constraints:
1 ≤ K ≤ N ≤ 105 

-104 ≤ X, arr[i] ≤ 104

### Topic: Heap

### Hint 1
Make a max heap of k houses with custom Compare function that firstly gives priority to maximum distance but if the two distances are same then priority is given to house with greater house number. 

### Hint 2
1) Make a max heap with first k elements.
2) For every element from (k+1)th to nth, do the following.

…..a) Find difference of current element with x.

…..b) If difference is more than root of heap, ignore current element.

…..c) Else insert the current element to the heap after removing the root.

3) Finally the heap has k closest elements.
