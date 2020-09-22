# 152. Maximum Product Subarray
## Medium
### Array/Dynamic Programming
#
Relative: [53](https://github.com/Yiyang-C/LeetCode/blob/master/0053_Maximum%20Subarray.md), 198, 238, 628, 713, 
#

Given an integer array ```nums```, find the contiguous subarray within an array (containing at least one number) which has the largest product.

Example1:
> Input: [2,3,-2,4]
> 
> Output: 6
>
> Explanation: [2,3] has the largest product 6.

Example2:
> Input: [-2,0,-1]
> 
> Output: 0
>
> Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

**My Note:**
* DP/ State machine

Solution1:
*Time: O(n)*
*Space: O(1)*
```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        posi = nega = nums[0]
        for i in range(1, len(nums)):
            num = nums[i]
            cur_posi = max(num, num*posi, num*nega)
            cur_nega = min(num, num*posi, num*nega)
            posi, nega = cur_posi, cur_nega
            res = max(cur_posi, res)
        return res
```
