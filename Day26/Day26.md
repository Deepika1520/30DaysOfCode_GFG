## Project Manager
An IT company is working on a large project. The project is broken into N modules and distributed to different teams. The amount of time (in months) required to complete each module is given in an array duration[ ]. Two modules can be processed simultaneously only if their is no dependency between them and it is given that M modules have interdependecies. 
As the project manager, compute the minimum time required to complete the project.

### Example 1:
Input:
N = 6 6
duration[] = {1, 2, 3, 1, 3, 2}
dependencies:
5 2
5 0
4 0 
4 1
2 3
3 1
Output: 
8
Explanation: 

![alt text](https://media.geeksforgeeks.org/wp-content/cdn-uploads/graph.png)

The Graph of dependency forms this and the project will be completed when Module 1 is completed which takes 8 months.

### Example 2:
Input:
N = 3 3

duration[] = {5, 5, 5}

dependencies:
0 1

1 2

2 0

Output: -1

Explanation: There is a cycle in the dependency graph hence the project cannot be completed.

### Your Task:
Complete the function minTime() which takes N, M, duration array, and dependencies array as input parameter and return the minimum time required. Return -1 if the project can not be completed. 

### Expected Time Complexity: O(N)
### Expected Auxiliary Space: O(N)

### Constraints:
1 ≤ N ≤ 105

1 ≤ M ≤ 2*105

1 ≤ duration[i] ≤ 105

### Topic:  DFS, Graph, Sorting

### Hint
Use topological sorting. Check for cycle, and use back tracking dfs to calculate the answer.
