# 1291. Sequential Digits
## Medium
### Backtracking
#

An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a **sorted** list of all the integers in the range ```[low, high]``` inclusive that have sequential digits.

Example1:
> Input: low = 100, high = 300
> 
> Output: [123,234]

Example2:
> Input: low = 1000, high = 13000
> 
> Output: [1234,2345,3456,4567,5678,6789,12345]

**Constraints:** 
* ```10 <= low <= high <= 10^9```

**My Note:**
* Typical Backtracking
* Iterate the length

Solution1:
```python
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        self.res = []
        l = len(str(low))
        r = len(str(high))
        
        def helper(cur, l):
            if cur:
                if len(cur) > l or int(cur) > high:
                    return
                if low <= int(cur) <= high and len(cur) == l:
                    self.res.append(int(cur))
                    return
            if not cur:
                for i in range(1, 10):
                    helper(str(i), l)
            else:
                tmp = int(cur[-1]) + 1
                if tmp == 10:
                    return
                helper(cur+str(tmp), l)
        
        for i in range(l, r+1):
            helper('', i)
        return self.res
```
