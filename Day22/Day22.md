## Shortest Range In BST
Given a BST (Binary Search Tree), find the shortest range [x, y], such that, at least one node of every level of the BST lies in the range.
If there are multiple ranges with the same gap (i.e. (y-x)) return the range with the smallest x.

### Example 1:
Input:

            8
          /   \
         3     10
       /  \      \
      2    6      14
          / \     /
         4   7   12
                /  \
               11   13
               
Output: 6 11

Explanation: Level order traversal of the tree is [8], [3, 10], [2, 6, 14], [4, 7, 12], [11, 13]. The shortest range which satisfies the above mentioned condition is [6, 11]. 

### Example 2:
Input:

   12
  
    \
     
     13
     
        \
        
        14
        
          \
          
          15
          
            \
            
             16
           

Output: 12 16

Explanation: Each level contains one node, so the shortest range is [12, 16].

### Your Task:
You don't need to read input or print anything. Complete the function shortestRange() which takes the root of the tree as an input parameter and returns the pair of numbers

### Expected Time Complexity: O(N)
### Expected Auxiliary Space: O(N)

### Constraints:
1 ≤ N ≤ 105

1 ≤ Node Value ≤ 104

### Topics- Two-Pointer Algorithm Binary Search Tree Trees

### Hint
Use two pointer technique in inorder traversal of the tree. 
Set left pointer at first index and right pointer at root's index in inorder traversal of the bst. 
Then check if the current range contains all levels if yes the shift left pointer 1 index right, otherwise increase the right pointer by 1. 
Continue this process till left pointer reaches the root's index or right pointer reaches last index.
