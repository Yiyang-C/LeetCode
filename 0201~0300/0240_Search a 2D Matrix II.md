# 240. Search a 2D Matrix II
## Medium
### Binary Search/Divide and Conquer
#
Relative: [74](https://github.com/Yiyang-C/LeetCode/blob/master/0001~0100/0074_Search%20a%202D%20Matrix.md)
#

Write an efficient algorithm that searches for a value in an *m x n* matrix. This matrix has the following properties:

* Integers in each row are sorted in ascending from left to right.
* Integers in each column are sorted in ascending from top to bottom.

Example:
> Consider the following matrix:
```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```
> Given target = ```5```, return ```true```.
>
> Given target = ```20```, return ```false```.

**My Note:**
* Start from the up-right corner of the matrix
* if the value is larger than the target move downward
* if the value is smaller than the target move leftward
* if outside the border return ```False```

Solution1:
*Time: O(m + n)*
*Space: O(1)*
```python
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0]:
            return False
        m, n = len(matrix), len(matrix[0])
        i, j = 0, n - 1
        
        while True:
            if i >= m or j < 0:
                return False
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                i += 1
            else:
                j -= 1
```
