# 266. Palindrome Permutation
## Easy
### Hash Table
#
Relative: 5, 242, 267, 409
#

Given a string, determine if a permutation of the string could form a palindrome.

Example1:
> Input: "code"
> 
> Output: false

Example2:
> Input: "aab"
> 
> Output: true

Example3:
> Input: "carerac"
> 
> Output: true

**My Note:**
* Counter
* The #occurence should only have one or no odd number

Solution:
*Time: O(n)*
*Space: O(n)*
```python
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        c = collections.Counter(s)
        f = 0
        for ch in c:
            if c[ch] % 2:
                f += 1
        return f <= 1
 ```
