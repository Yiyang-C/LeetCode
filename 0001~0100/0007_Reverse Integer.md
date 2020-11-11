# 7. Reverse Integer
## Easy
### Math
#
Relative: 8, 190
#

Given a 32-bit signed integer, reverse digits of an integer.

**Note:**

Assume we are dealing with an environment that could only store integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

Example1:
> Input: x = 123
> 
> Output: 321

Example2:
> Input: x = -123
> 
> Output: -321

Example3:
> Input: x = 120
> 
> Output: 21

Example4:
> Input: x = 0
> 
> Output: 0

**Constraints:** 
* ```-231 <= x <= 231 - 1```

**My Note:**
* Convert int into str then reverse it
* Convert reversed str into int

Solution:
*Time: O(n)*
*Space: O(n)*
```python
class Solution:
    def reverse(self, x: int) -> int:
        if x < 0:
            res = -int(str(x)[1:][::-1])
            return res if res >= -2**31 else 0
        else:
            res = int(str(x)[::-1])
            return res if res <= 2**31 - 1 else 0
```
