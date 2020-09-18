# 53. Maximum Subarray
## Easy
### Array/Divid and Conquer/Dynamic Programming
#
Relative: [121](https://github.com/Yiyang-C/LeetCode/blob/master/0121_Best%20Time%20to%20Buy%20and%20Sell%20Stock.md), 152, 697, 978
#

Given an integer array ```nums```, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Follow up:** If you have figured out the O(n) solution, try coding another solution using the **divide and conquer** approach, which is more subtle.

Example1:
> Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
> 
> Output: 6
>
> Explanation: [4,-1,2,1] has the largest sum = 6.

Example2:
> Input: nums = [1]
> 
> Output: 1

Example3:
> Input: nums = [0]
> 
> Output: 0

Example4:
> Input: nums = [-1]
> 
> Output: -1

Example5:
> Input: nums = [-2147483647]
> 
> Output: -2147483647

**Constraints:** 
* ```1 <= nums.length <= 2 * 10^4```
* ```-2^31 <= nums[i] <= 2^31 - 1```


**My Note:**
* DP

Solution1:
*Time: O(n)*
*Space: O(1)*
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res = tmp = -float('inf')
        for num in nums:
            tmp = max(num, tmp + num)
            res = max(tmp, res)
        return res
```

**My Note:**
* DC

Solution2:
*Time: O(nlogn)*
*Space: O(n)*
```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.dchepler(nums, 0, len(nums) - 1)
    
    def dchepler(self, nums, l, r):
        if l > r:
            return -float('inf')
        m = (l + r) >> 1
        ml = mr = 0
        lmax = self.dchepler(nums, l, m-1)
        rmax = self.dchepler(nums, m+1, r)
        total = 0
        for i in range(l, m)[::-1]:
            total += nums[i]
            ml = max(ml, total)
        total = 0
        for i in range(m+1, r+1):
            total += nums[i]
            mr = max(mr, total)
        return max(lmax, rmax, ml + mr + nums[m])
```
