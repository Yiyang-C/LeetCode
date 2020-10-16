# 74. Search a 2D Matrix
## Medium
### Array/Binary Search
#
Relative: 240
#

Write an efficient algorithm that searches for a value in an ```m x n``` matrix. This matrix has the following properties:

* Integers in each row are sorted from left to right.
* The first integer of each row is greater than the last integer of the previous row.

Example1:

![img1](https://assets.leetcode.com/uploads/2020/10/05/mat.jpg)
> Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 3
> 
> Output: true

Example2:

![img2](https://assets.leetcode.com/uploads/2020/10/05/mat2.jpg)
> Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]], target = 13  
> 
> Output: false

Example3:
> Input: matrix = [], target = 0
> 
> Output: false

**Constraints:** 
* ```m == matrix.length```
* ```n == matrix[i].length```
* ```0 <= m, n <= 100```
* ```-10^4 <= matrix[i][j], target <= 10^4```

**My Note:**
* Using binary search to find the row which the target may exist
* Note that ```mid = ((top + bot) >> 1) + 1```
* Using binary search to determine if the target exsit in this row

Solution1:
*Time: O(lgm + lgn)*
*Space: O(1)*
```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        m, n = len(matrix), len(matrix[0])
        if not m or not n:
            return False
        top, bot = 0, m - 1
        while top < bot:
            mid = ((top + bot) >> 1) + 1
            if matrix[mid][0] == target:
                return True
            if matrix[mid][0] > target:
                bot = mid - 1
            else:
                top = mid
                
        left, right = 0, n - 1
        while left < right:
            mid = (left + right) >> 1
            if matrix[top][mid] == target:
                return True
            if matrix[top][mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        if matrix[top][left] == target:
            return True
        return False
```
