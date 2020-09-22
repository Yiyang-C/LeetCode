# 216. Combination Sum III
## Medium
### Array/Backtracking
#

Find all possible combinations of **k** numbers that add up to a number **n**, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.

**Note:**
* The solution set must not contain duplicate combinations.

Example1:
> Input: k = 3, n = 7
> 
> Output: [[1,2,4]]
    
Example2:
> Input: k = 3, n = 9
> 
> Output: [[1,2,6],[1,3,5],[2,3,4]]
    
Example3:
> Input: k = 4, n = 1
> 
> Output: []
    
Example2:
> Input: k = 9, n = 45
> 
> Output: [[1,2,3,4,5,6,7,8,9]]
    
**Constraints:**
* 2 <= k <= 9
* 1 <= n <= 60

**My Note:**
* Typical Backtracking

Solution:
```python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.res = []
        self.helper('', n, k)
        return self.res
        
    def helper(self, combo, remain, k):
        # print(combo)
        if len(combo) == k:
            if not remain:
                self.res.append(combo)
            return
        # elif not remain:
        #     return
        if combo:
            for num in range(int(combo[-1])+1, min(10, remain+1)):
                self.helper(combo+str(num), remain - num, k)
        else:
            for num in range(1, min(10, remain+1)):
                self.helper(combo+str(num), remain - num, k)
```
