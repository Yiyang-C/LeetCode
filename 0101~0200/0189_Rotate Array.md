# 189. Rotate Array
## Medium
### Array
#
Relative: 61, 186
#

Given an array, rotate the array to the right by k steps, where k is non-negative.

**Follow up:** 
* Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
* Could you do it in-place with O(1) extra space?

Example1:
> Input: nums = [1,2,3,4,5,6,7], k = 3
> 
> Output: [5,6,7,1,2,3,4]
>
> Explanation: 
>
> rotate 1 steps to the right: [7,1,2,3,4,5,6]
>
> rotate 2 steps to the right: [6,7,1,2,3,4,5]
>
> rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example2:
> Input: nums = [-1,-100,3,99], k = 2
> 
> Output: [3,99,-1,-100]
>
> Explanation: 
>
> rotate 1 steps to the right: [99,-1,-100,3]
>
> rotate 2 steps to the right: [3,99,-1,-100]

**Constraints:** 
* ```1 <= nums.length <= 2 * 10^4```
* ```-2^31 <= nums[i] <= 2^31 - 1```
* ```0 <= k <= 10^5```

<details><summary>Hint1</summary>
The easiest solution would use additional memory and that is perfectly fine.
</details>

<details><summary>Hint2</summary>
The actual trick comes when trying to solve this problem without using any additional memory. This means you need to use the original array somehow to move the elements around. Now, we can place each element in its original location and shift all the elements around it to adjust as that would be too costly and most likely will time out on larger input arrays.
</details>

<details><summary>Hint3</summary>
One line of thought is based on reversing the array (or parts of it) to obtain the desired result. Think about how reversal might potentially help us out by using an example.
</details>

<details><summary>Hint4</summary>
The other line of thought is a tad bit complicated but essentially it builds on the idea of placing each element in its original position while keeping track of the element originally in that position. Basically, at every step, we place an element in its rightful position and keep track of the element already there or the one being overwritten in an additional variable. We can't do this in one linear pass and the idea here is based on **cyclic-dependencies** between elements.
</details>

Solution1:
*Time: O(n)*
*Space: O(n)*
```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
```

Solution2:
*Time: O(n)*
*Space: O(1)*
```python
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k %= len(nums)
        self.reverse(nums, 0, len(nums)-1)
        self.reverse(nums, 0, k-1)
        self.reverse(nums, k, len(nums)-1)
    
    def reverse(self, nums, l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1
```
