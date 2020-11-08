# 1099. Two Sum Less Than K
## Easy
### Array/Two Pointers/Sort
#
Relative: [1](https://github.com/Yiyang-C/LeetCode/blob/master/0001~0100/0001_Two%20Sum.md), 167, 259, 713
#

Given an array ```A``` of integers and integer ```K```, return the maximum S such that there exists ```i < j``` with ```A[i] + A[j] = S``` and ```S < K```. If no ```i, j``` exist satisfying this equation, return ```-1```.

Example1:
> Input: A = [34,23,1,24,75,33,54,8], K = 60
> 
> Output: 58
>
> Explanation: We can use 34 and 24 to sum 58 which is less than 60.

Example2:
> Input: A = [10,20,30], K = 15
> 
> Output: -1
>
> Explanation: In this case it is not possible to get a pair sum less that 15.

**Constraints:** 
* ```1 <= A.length <= 100```
* ```1 <= A[i] <= 1000```
* ```1 <= K <= 2000```

<details><summary>Hint1</summary>
What if we have the array sorted?
</details>

<details><summary>Hint2</summary>
Loop the array and get the value A[i] then we need to find a value A[j] such that A[i] + A[j] < K which means A[j] < K - A[i]. In order to do that we can find that value with a binary search.
</details>

**My Note:**
* Sort
* Two pointers

Solution1:
*Time: O(nlogn)*
*Space: O(1)*
```python
class Solution:
    def twoSumLessThanK(self, A: List[int], K: int) -> int:
        A.sort()
        l, r, res = 0, len(A) - 1, -1
        while l < r:
            if A[l] + A[r] >= K:
                r -= 1
            else:
                res = max(A[l] + A[r], res)
                l += 1
        return res
```
