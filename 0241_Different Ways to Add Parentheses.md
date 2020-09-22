# 241. Different Ways to Add Parentheses
## Medium
### Divide and Conquer
#
Relative: 85, 224, 282
#

Given a string of numbers and operators, return all possible results from computing all the different possible ways to group numbers and operators.The valid operators are ```+```, ```-``` and ```*```.

Example1:
> Input: "2-1-1"
> 
> Output: [0, 2]
>
> Explanation:
>
> ((2-1)-1) = 0 
>
> (2-(1-1)) = 2

Example2:
> Input: "2*3-4*5"
> 
> Output: [-34, -14, -10, -10, 10]
>
> Explanation:
>
> (2*(3-(4*5))) = -34 
>
> ((2*3)-(4*5)) = -14 
>
> ((2*(3-4))*5) = -10 
>
> (2*((3-4)*5)) = -10 
>
> (((2*3)-4)*5) = 10

**My Note:**
* Recurse itself
* If only digit return itself
* Else iterate the characters in the string
* If its ```+```, ```-``` or ```*``` divide the string to operate
* [LeetCode Discuss](https://leetcode.com/problems/different-ways-to-add-parentheses/discuss/66419/Python-easy-to-understand-solution-(divide-and-conquer).)

Solution1:
*Time: O(n)*
*Space: O(n)*
```python
class Solution:
    def diffWaysToCompute(self, input: str) -> List[int]:
        if input.isdigit():
            return [int(input)]
        res = []
        for i in range(len(input)):
            if input[i] in "-+*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for j in res1:
                    for k in res2:
                        res.append(self.helper(j, k, input[i]))
        return res

    def helper(self, m, n, op):
        if op == "+":
            return m+n
        elif op == "-":
            return m-n
        else:
            return m*n
```

**My Note:**
* Store the tmp result to save time

Solution2:
*Time: O(n)*
*Space: O(n)*
```python
class Solution:    
    def diffWaysToCompute(self, input, memo={}):
        if input.isdigit():
            return [int(input)]
        if input in memo:
            return memo[input] 
        res = []
        for i in range(len(input)):
            if input[i] in "-+*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i+1:])
                for j in res1:
                    for k in res2:
                        res.append(self.helper(j, k, input[i]))
        memo[input] = res
        return res

    def helper(self, m, n, op):
        if op == "+":
            return m+n
        elif op == "-":
            return m-n
        else:
            return m*n

```
