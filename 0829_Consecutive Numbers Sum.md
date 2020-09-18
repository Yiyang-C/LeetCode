# 829. Consecutive Numbers Sum
## Hard
### Math
#

Given a positive integer ```N```, how many ways can we write it as a sum of consecutive positive integers?

Example1:
> Input: 5
> 
> Output: 2
>
> Explanation: 5 = 5 = 2 + 3

Example2:
> Input: 9
> 
> Output: 3
>
> Explanation: 9 = 9 = 4 + 5 = 2 + 3 + 4

Example3:
> Input: 15
> 
> Output: 4
>
> Explanation: 15 = 15 = 8 + 7 = 4 + 5 + 6 = 1 + 2 + 3 + 4 + 5

**Note:** 
* ```1 <= N <= 10 ^ 9```

**My Note:**
* [LeetCode Discuss](https://leetcode.com/problems/consecutive-numbers-sum/discuss/128959/JavaPython-3-5-liners-O(N-0.5)-Math-method-w-explanation-and-analysis.)
* N = k + (k+1) + (k+2) + ... + (k + i - 1) [i items]
* N = k * i + i * (i - 1) / 2
* k = N / i - (i - 1) / 2 > 0
* N > i * (i - 1) / 2

Solution1:
*Time: O(n^0.5)*
*Space: O(1)*
```python
class Solution:
    def consecutiveNumbersSum(self, N: int) -> int:
        res, i = 0, 1
        while N > (i - 1) * i // 2:
            if not ((N - (i - 1) * i // 2) % i):
                res += 1
            i += 1
        return res
```
