# 384. Shuffle an Array
## Medium
### 
#

Shuffle a set of numbers without duplicates.

> // Init an array with set 1, 2, and 3.
>
> int[] nums = {1,2,3};
>
> Solution solution = new Solution(nums);
>
> </br>
> // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
>
> solution.shuffle();
>
></br>
> // Resets the array back to its original configuration [1,2,3].
>
> solution.reset();
>
></br>
> // Returns the random shuffling of array [1,2,3].
>
> solution.shuffle();

**My Note:**
* random.sample

Solution1:
*Time: O(n)*
*Space: O(n)*
```python
class Solution:

    def __init__(self, nums: List[int]):
        self.origin = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.origin

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        return random.sample(self.origin, len(self.origin))


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
```
