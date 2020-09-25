# 179. Largest Number
## Medium
### Sort
#

Given a list of non negative integers, arrange them such that they form the largest number.

Example1:
> Input: [10,2]
> 
> Output: "210"

Example2:
> Input: [3,30,34,5,9]
> 
> Output: "9534330"

**Note:** 
The result may be very large, so you need to return a string instead of an integer.

**My Note:**
* Using cmp_to_key

Solution1:
*Time: O(nlogn)*
*Space: O(n)*
```python
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not sum(nums):
            return '0'
        nums = [str(num) for num in nums]
        nums.sort(key = cmp_to_key(lambda x,y: int(y+x) - int(x+y)))
        return ''.join(nums)
```
