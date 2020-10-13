# 459. Repeated Substring Pattern
## Easy
### String
#
Relative: 28, 686
#

Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.

Example1:
> Input: "abab"
> 
> Output: True
>
> Explanation: It's the substring "ab" twice.

Example2:
> Input: "aba"
> 
> Output: False

Example3:
> Input: "abcabcabcabc"
> 
> Output: True
>
> Explanation: It's the substring "abc" four times. (And the substring "abcabc" twice.)

**My Note:**
* Examine all substrings
* From the longest to the shortest

Solution:
*Time: O(n)*
*Space: O(1)*
```python
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        i = n - 1
        while i > 0:
            if not n % i:
                if s == s[:i] * (n // i):
                    return True
            i -= 1
        return False
```
