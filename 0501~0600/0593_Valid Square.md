# 593. Valid Square
## Medium
### Math
#

Given the coordinates of four points in 2D space, return whether the four points could construct a square.

The coordinate (x,y) of a point is represented by an integer array with two integers.

Example:
> Input: p1 = [0,0], p2 = [1,1], p3 = [1,0], p4 = [0,1]
> 
> Output: True

**Note:** 
* All the input integers are in the range [-10000, 10000].
* A valid square has four equal sides with positive length and four equal angles (90-degree angles).
* Input points have no order.

**My Note:**
![img](https://assets.leetcode.com/users/images/93aa5df8-fb38-43e6-86d0-476a0b4fe7a9_1605082521.9208896.png)
* Check edge length between each point pair:
* Accept if there are only two kinds of edge length, one is side length (the black ones), the other is diagonal length (the gray ones).
* Reject if there are repeated points.
* [LeetCode Discuss](https://leetcode.com/problems/valid-square/discuss/931657/Python-sol-by-checking-edge-length-w-Visualization)

Solution1:
*Time: O(1)*
*Space: O(1)*
```python
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        l = [p1, p2, p3, p4]
        s = set()
        for i in range(3):
            for j in range(i+1,4):
                cur_length = ((l[i][0] - l[j][0]) ** 2 + (l[i][1] - l[j][1]) ** 2) ** 0.5
                if cur_length == 0:
                    return False
                s.add(cur_length)
        return len(s) == 2
```
