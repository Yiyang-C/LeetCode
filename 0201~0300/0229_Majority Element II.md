# 229. Majority Element II
## Medium
### Array
#
Relative: 169, 1150
#

Given an integer array of size n, find all elements that appear more than ```⌊ n/3 ⌋``` times.

**Note:**
The algorithm should run in linear time and in O(1) space.

Example1:
> Input: [3,2,3]
> 
> Output: [3]

Example2:
> Input: [1,1,1,3,3,2,2,2]
>
> Output: [1,2]

<details><summary>Hint1</summary>
How many majority elements could it possibly have?</details>

**My Note:**
* No more than two majority elements

Solution1:
*Time: O(n)*
*Space: O(1)*
```python
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ans = [None] * 2
        vote = [0] * 2
        for num in nums: 
            if not vote[0] and num not in ans:
                ans[0] = num
            elif not vote[1] and num not in ans:
                ans[1] = num
            
            if ans[0] == num:
                vote[0] += 1
            elif ans[1] == num:
                vote[1] += 1
            else: vote = [num-1 for num in vote]
        return [num for num in ans if nums.count(num) > len(nums)//3]
```
