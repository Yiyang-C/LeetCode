# 1249. Minimum Remove to Make Valid Parentheses
## Medium
### String/Stack
#

Given a string s of ```'('``` , ```')'``` and lowercase English characters. 

Your task is to remove the minimum number of parentheses ( ```'('``` or ```')'```, in any positions ) so that the resulting parentheses string is valid and return **any** valid string.

Formally, a *parentheses string* is valid if and only if:
* It is the empty string, contains only lowercase characters, or
* It can be written as ```AB``` (```A``` concatenated with ```B```), where ```A``` and ```B``` are valid strings, or
* It can be written as ```(A)```, where ```A``` is a valid string.

Example1:
> Input: s = "lee(t(c)o)de)"
> 
> Output: "lee(t(c)o)de"
>
> Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example2:
> Input: s = "a)b(c)d"
> 
> Output: "ab(c)d"

Example3:
> Input: "))(("
> 
> Output: ""
>
> Explanation: An empty string is also valid.

Example4:
> Input: s = "(a(b(c)d)"
> 
> Output: "a(b(c)d)"

**Constraints:** 
* ```1 <= s.length <= 10^5```
* ```s[i]``` is one of  ```'('``` , ```')'``` and lowercase English letters.

<details><summary>Hint1</summary>
Each prefix of a balanced parentheses has a number of open parentheses greater or equal than closed parentheses, similar idea with each suffix.
</details>

<details><summary>Hint2</summary>
Check the array from left to right, remove characters that do not meet the property mentioned above, same idea in backward way.
</details>

**My Note:**
* Check all parentheses from left to right

Solution:
*Time: O(n)*
*Space: O(n)*
```python
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = ''
        cnt = i = 0
        position = []
        while s:
            ch = s[0]
            if ch == '(':
                cnt += 1
                position.append(i)
            elif ch == ')':
                if cnt:
                    cnt -= 1
                else:
                    # i += 1
                    s = s[1:]
                    continue
            res += ch
            i += 1
            s = s[1:]
        while cnt:
            p = position.pop()
            res = res[:p] + res[p+1:]
            cnt -= 1
        return res
```
