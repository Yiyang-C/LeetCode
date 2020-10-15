# 198. House Robber
## Easy
### Dynamic Programming
#
Relative: [152](https://github.com/Yiyang-C/LeetCode/blob/master/0101~0200/0152_Maximum%20Product%20Subarray.md), [213](https://github.com/Yiyang-C/LeetCode/blob/master/0201~0300/0213_House%20Robber%20II.md), 256, 276, 337, 600, 656, 740
#

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Example1:
> Input: nums = [1,2,3,1]
> 
> Output: 4
>
> Explanation: 
>
> Rob house 1 (money = 1) and then rob house 3 (money = 3).
>
> Total amount you can rob = 1 + 3 = 4.

Example2:
> Input: nums = [2,7,9,3,1]
> 
> Output: 12
>
> Explanation: 
>
> Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
>
> Total amount you can rob = 2 + 9 + 1 = 12.

**Constraints:** 
* ```0 <= nums.length <= 100```
* ```0 <= nums[i] <= 400```

**My Note:**
* Typical DP problem

Solution1:
*Time: O(n)*
*Space: O(n)*
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        dp = [0 for _ in range(len(nums))]
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
        return dp[-1]
```
