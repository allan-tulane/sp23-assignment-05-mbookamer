# CMPS 2200 Assignment 5
## Answers

**Name:** Mackenzie Bookamer


Place all written answers from `assignment-05.md` here for easier grading.





- **1a.**

The greedy algorithms would involve figuring out what power of 2 is the highest such that 2^k is less than N. We recursively repeat this process until we 
get a final answer that adds up to N. Since all coins are powers of 2, this algorithm is optimal. 


- **1b.**
The work and span of this algorithm are both O(log n) because we are dividing our number N by powers of 2, so our work becomes this. Since the algorithm is 
not parallelizable, the span is also O(log n).

- **2a.**
Let's say for instance we are have 11 dollars, and the denominations of coins are 1,3,4,7,9. The greedy algorithm would choose 9 first, then 1, then 1 again. However, the optimal solution would be choosing 7 first and then 4. We see that 7 is the second highest denomination, and unlike our algorithm in 1a, there is no real pattern connecting the denominations to each other, so we cannot assume the highest denomination yields the optimal solution. 

- **2b.**
This new program would look at both the highest and second highest denomination and yield a tree of possibilities with the children being the denominations that would be chosen to get to our total number N. I would then calculate the length of the path from the root (N) to the leaf on the left and right side (second highest and highest denomination respectively). The shortest path would yield the optimal solution. However, this could lead to subproblems being recomputed, so instead, we keep our tree the same and create a dictionairy of the difference at each intermediate level and how many steps it took to get there. The dynamic programming algorithm would then return the shortest path to get to N, so in essence, the solution obtained when thinking about our problem as a tree. The work and span of this algorithm would both be O(n) since we have to iterate over all possible solutions. 

- **3a.**


Implemented in main.py



- **3b.**


Implemented in main.py



- **3c.**


Implemented in main.py
