# 1. Two Sum
## Easy
### Array/Hash Table
#
Relative: [15](https://github.com/Yiyang-C/LeetCode/blob/master/0001~0100/0015_3Sum.md), [18](https://github.com/Yiyang-C/LeetCode/blob/master/0001~0100/0018_4Sum.md), 167, [170](https://github.com/Yiyang-C/LeetCode/blob/master/0101~0200/0170_Two%20Sum%20III%20-%20Data%20structure%20design.md), 560, 653, 1099
#

Given an array of integers ```nums``` and an integer ```target```, return indices of the two numbers such that they add up to ```target```.

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

Example1:
> Input: nums = [2,7,11,15], target = 9
> 
> Output: [0,1]
>
> Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example2:
> Input: nums = [3,2,4], target = 6
> 
> Output: [1,2]

Example3:
> Input: nums = [3,3], target = 6
> 
> Output: [0,1]

**Constraints:** 
* ```2 <= nums.length <= 10^5```
* ```-10^9 <= nums[i] <= 10^9```
* ```-10^9 <= target <= 10^9```
* **Only one valid answer exists.**

**My Note:**
* HashMap

Solution1:
*Time: O(n)*
*Space: O(n)*
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            d[target - num] = i
        for i, num in enumerate(nums):
            if num in d and i != d[num]:
                return i, d[num]
```

**My Note:**
* HashMap
* Traverse once

Solution2:
*Time: O(n)*
*Space: O(n)*
```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            if target-num in d:
                return d[target-num], i
            d[num] = i
```
