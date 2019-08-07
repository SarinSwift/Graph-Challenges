## Graphs Data Structure

#### Challenge 1
- Implements the graph ADT with an adjacency list.
- Implements code to read in an instance of a graph and uses its methods  
ex.
```
G
1,2,3,4
(1,2,10)
(1,4,5)
(2,3,5)
(2,4,7)
```
Output.
```
# Vertices: 4
# Edges: 4
Edge List:
(1,2,10)
(1,4,5)
(2,3,5)
(2,4,7)
```

#### Challenge 2
- Implement breadth first search to to compute the shortest path between 2 provided vertices   
ex.
```
G
1,2,3,4,5
(1,2)
(1,4)
(2,3)
(2,4)
(2,5)
(3,5)
```
Output.
```
Vertices in shortest path: 1,2,5
Number of edges in shortest path: 2
```

#### Challenge 3
- Implements Iterative DFS and recursive DFS
- DFS finds if there is a path between 2 given vertices in a directed graph  
ex.
```
D
1,2,3,4,5
(1,2)
(1,4)
(2,3)
(2,4)
(3,5)
(5,2)
```
Output.
```
There exists a path between vertex 1 and 5: TRUE
Vertices in the path: 1,2,3,5
```

#### Challenge 4
Dynamic Programming Problems  

**5 Steps of Dynamic Programming:**
1. Find the first solution  
Just get something down on paper without needing to concern about the efficiency.    
Things to concern are: the solution should be recursive, and the results of each call should be self contained(meaning that you shouldn't store results to a global variable), and lastly, we should minimize the number of parameters in the function.

2. Analyze the first solution  
Mostly looking at a solution when it is mostly exponential time or worse in efficiency.  
Dynamic programming requires to meet 2 criteria:   
    - Optimal structure - We should be able to figure out the solution recursively.
    - Overlapping sub problems - If we are calling the same function with the exact same input parameters multiple times. This means we're doing repetitive work for no reason. !!We can cache(memoize) the results to save a lot of time!!  


3. Identify the sub problems  
Look from the recursive function and see what calls are being made and the different inputs that are being changed.  
For example finding the fibonacci of n: fib(n-1) and fib(n-2) are the recursive calls.  
Once we know the recursive calls(sub problems), we can memoize the recursive solutions to make it more efficient. (Memoize==adding an array or hash maps to store all the values that have been computed already).  
Each time we make a recursive call, we look in the array or hash map if there is already a value in it. If there is, we can just return that value, otherwise, we can calculate the value and store one more new  value to our array/hash map

4. Turn around the solution  
Dynamic Programming generally has 2 ways to approach it:  
**A top down (memoized) solution: recursive** This is because we're starting at the goal result and then repeatedly splitting it into, normaly, 2 branches until we reach the base case!   
**A bottom up (tabular) solution: iterative** We start with the base case and then iteratively create larger sub problems until we reach the target result.


##### Example dynamic programming problems  

**1- Knapsack Problem**  
Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible.  
Using a set of problems that allows us to reuse previous solutions to smaller problems in order to calculate a solution to the current problem.  
- The knapsack problem can be seen by breaking it down in to 2 sub problems: where one case may be the knapsack containing the item, or the knapsack that doesn't contain the knapsack. And if the knapsack contains the item, we would need to decrease the bag's capacity as well as increase it's value.
- This function can be created by a recursive solution that takes in: Capacity, and an array of items. Where we can change both the input variables as we recursively call it.
- The sub problems are:   
```
value_without = knapsack(Capacity, items - curr_item)
value_with = knapsack(Capacity - item.weight, items - curr_item) + item.value
return max(value_without, value_with)
```
- Now, we can start creating the recursive function where we calculate the previous 2 sub problems.

**2- Minimum Path Sum(in a grid)**  
Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.  
Note: You can only move either down or right at any point in time.  
- Since you can only move either right, or downward, these are some cases we can repeat in each iteration, or recursion:
```
down = i+1, j
right = i, j+1
return min(down, right) + grid[i][j]
```
- we'd want to check the base cases where if the indexes are all the way on the last row and column, that means we can return straight away the value of the grid at indexes i and j. If it's on the last row, then we can only ever go right. If we're on the last column, means that we can only ever go down.
- So we can say that our recursive solution takes in the grid, the row's index (i), and lastly the columns index (j).
- The coding solution is in challenge_4.py file.
