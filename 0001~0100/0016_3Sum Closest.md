# 16. 3Sum Closest
## Medium
### Array/Two Pointers
#
Relative: [15](https://github.com/Yiyang-C/LeetCode/blob/master/0001~0100/0015_3Sum.md), 259
#

Given an array ```nums``` of n integers and an integer ```target```, find three integers in ```nums``` such that the sum is closest to ```target```. Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example1:
> Input: nums = [-1,2,1,-4], target = 1
> 
> Output: 2
>
> Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

**Constraints:** 
* ```3 <= nums.length <= 10^3```
* ```-10^3 <= nums[i] <= 10^3```
* ```-10^4 <= target <= 10^4```

**My Note:**
* Sort ```nums```
* Iterate to find the closest sum to target

Solution:
*Time: O(n^2)*
*Space: O(1)*
```python
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = sum(nums[:3])
        for i in range(len(nums) - 2):
            if i > 0  and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                tmp = nums[i] + nums[l] + nums[r]
                # print(i, l, r, tmp)
                if abs(tmp - target) < abs(res - target):
                    res = tmp
                    if tmp > target:
                        r -= 1
                        while l < r and nums[r+1] == nums[r]:
                            r -= 1
                    elif tmp < target:
                        l += 1
                        while l < r and nums[l-1] == nums[l]:
                            l += 1  
                elif tmp > target:
                    r -= 1
                elif tmp < target:
                    l += 1
                else:
                    break
        return res
```
