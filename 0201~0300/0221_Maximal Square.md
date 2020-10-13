# 221. Maximal Square
## Medium
### Dynamic Programming
#
Relative: 85, 764
#

Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:
> Input: 
> 
> 1 0 1 0 0
>
> 1 0 **1 1** 1
>
> 1 1 **1 1** 1
>
> 1 0 0 1 0
>
> Output: 4

**My Note:**
* Dynamic Programming
* 2D DP

Solution:
*Time: O(mn)*
*Space: O(mn)*
```python
class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        res = 0
        if not matrix:
            return res
        r, c = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(c+1)] for _ in range(r+1)]
        for i in range(r):
            for j in range(c):
                dp[i+1][j+1] = (min(dp[i][j], dp[i][j+1], dp[i+1][j]) + 1) * int(matrix[i][j])
                res = max(res, dp[i+1][j+1] ** 2)
        return res
```
