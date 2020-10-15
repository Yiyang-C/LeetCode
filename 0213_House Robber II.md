# 213. House Robber II
## Medium
### Dynamic Programming
#
Relative: [198](https://github.com/Yiyang-C/LeetCode/blob/master/0101~0200/0198_House%20Robber.md), 256, 276, 337, 600, 656
#

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are **arranged in a circle.** That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and **it will automatically contact the police if two adjacent houses were broken into on the same night**.

Given a list of non-negative integers ```nums``` representing the amount of money of each house, return the maximum amount of money you can rob tonight **without alerting the police**.

Example1:
> Input: nums = [2,3,2]
> 
> Output: 3
>
> Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Example2:
> Input: nums = [1,2,3,1]
> 
> Output: 4
>
> Explanation: 
> 
> Rob house 1 (money = 1) and then rob house 3 (money = 3).
>
> Total amount you can rob = 1 + 3 = 4.

Example3:
> Input: nums = [0]
> 
> Output: 0

**Constraints:**
* ```1 <= nums.length <= 100```
* ```0 <= nums[i] <= 1000```

<details><summary>Hint1</summary>
Since House[1] and House[n] are adjacent, they cannot be robbed together. Therefore, the problem becomes to rob either House[1]-House[n-1] or House[2]-House[n], depending on which choice offers more money. Now the problem has degenerated to the [House Robber](https://github.com/Yiyang-C/LeetCode/blob/master/0101~0200/0198_House%20Robber.md), which is already been solved.</details>

**My Note:**
* DP
* Two passes: House[1]-House[n-1] and House[2]-House[n]

Solution1:
*Time: O(n)*
*Space: O(n)*
```python
class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) <= 3:
            return max(nums)
        dp1 = [0 for _ in range(len(nums))]
        dp2 = [0 for _ in range(len(nums))]
        dp1[0] = dp1[1] = nums[0]
        for i in range(2, len(nums) - 1):
            dp1[i] = max(dp1[i-1], dp1[i-2] + nums[i])
        dp1[-1] = dp1[-2]
        for i in range(1, len(nums)):
            dp2[i] = max(dp2[i-1], dp2[i-2] + nums[i])
        # print(dp1, dp2)
        return max(dp1[-1], dp2[-1])
```
