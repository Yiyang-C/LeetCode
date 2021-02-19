# 413. Arithmetic Slices
## Medium
### Math/Dynamic Programming
#
Relative: 446
#

A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, these are arithmetic sequences:
```
1, 3, 5, 7, 9
7, 7, 7, 7
3, -1, -5, -9
```
The following sequence is not arithmetic.
```
1, 1, 2, 5, 7
```
A zero-indexed array A consisting of N numbers is given. A slice of that array is any pair of integers (P, Q) such that 0 <= P < Q < N.

A slice (P, Q) of the array A is called arithmetic if the sequence:
A[P], A[P + 1], ..., A[Q - 1], A[Q] is arithmetic. In particular, this means that P + 1 < Q.

The function should return the number of arithmetic slices in the array A.

**Example:**
```
A = [1, 2, 3, 4]

return: 3, for 3 arithmetic slices in A: [1, 2, 3], [2, 3, 4] and [1, 2, 3, 4] itself.
```

**My Note:**
* Check all parentheses from left to right

Solution:
*Time: O(n)*
*Space: O(n)*
```python
class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        pre = None
        dif = float('inf')
        l = []
        cnt = 2
        for num in A:
            if pre is not None:
                tmp = num - pre
                if tmp == dif:
                    cnt += 1
                else:
                    dif = tmp
                    if cnt >= 3:
                        l.append(cnt)
                    cnt = 2
            pre = num
        l.append(cnt)
        
        def helper(num):
            i = 1
            total = 0
            while num >=3:
                total += i
                i += 1
                num -= 1
            return total
        
        res = 0
        for cnt in l:
            res += helper(cnt)  
        return res
```
