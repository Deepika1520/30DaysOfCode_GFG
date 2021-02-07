## Check Tree Traversal
Given Preorder, Inorder and Postorder traversals of some tree of size N. The task is to check if they are all of the same tree or not.

### Example 1:
Input:

N = 5 

preorder[] = {1, 2, 4, 5, 3}

inorder[] = {4, 2, 5, 1, 3}

postorder[] = {4, 5, 2, 3, 1}

Output: Yes

Explanation: 
All of the above three traversals are of the same tree.

           1
         /   \
        2     3
      /   \
     4     5
     
### Example 2:
Input:

N = 5

preorder[] = {1, 5, 4, 2, 3}

inorder[] = {4, 2, 5, 1, 3}

postorder[] = {4, 1, 2, 3, 5}

Output: No

Explanation: The three traversals can not be of the same tree.

### Your Task:
You don't need to read input or print anything. Complete the function checktree() which takes the array preorder[ ], inorder[ ], postorder[ ] and integer N as input parameters and returns true if the three traversals are of the same tree or not. 

### Expected Time Complexity: O(N2)
### Expected Auxiliary Space: O(N)

### Constraints:

1 ≤ N ≤ 103
