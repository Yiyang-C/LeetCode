# 392. Is Subsequence
## Easy
### Binary Search/Dynamic Programming/Greedy
#
Relative: 792, 1055
#

Given two strings ```s``` and ```t```, check if ```s``` is a **subsequence** of ```t```.

A **subsequence** of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., ```"ace"``` is a subsequence of ```"abcde"``` while ```"aec"``` is not).

Example1:
> Input: s = "abc", t = "ahbgdc"
> 
> Output: true

Example2:
> Input: s = "axc", t = "ahbgdc"
> 
> Output: false

**Constraints:** 
* ```0 <= s.length <= 100```
* ```0 <= t.length <= 10^4```
* ```s``` and ```t``` consist only of lowercase English letters.

**Follow up:**
If there are lots of incoming ```s```, say ```s1, s2, ..., sk``` where ```k >= 10^9```, and you want to check one by one to see if ```t``` has its subsequence. In this scenario, how would you change your code?

**My Note:**
* Two Pointers

Solution:
*Time: O(nm)*
*Space: O(1)*
```python
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        i = j = 0
        while i < len(t) and j < len(s):
            if t[i] == s[j]:
                if j == len(s)-1:
                    return True
                i += 1
                j += 1
            else:
                i += 1
        return False
```
