# 389. Find the Difference
## Easy
### Hash Table/Bit Manipulation
#
Relative: 136
#

Given two strings **s** and **t** which consist of only lowercase letters.

String **t** is generated by random shuffling string **s** and then add one more letter at a random position.

Find the letter that was added in **t**.

Example1:
> Input:
>
> s = "abcd"
>
> t = "abcde"
> 
> Output: e
>
> Explanation: 'e' is the letter that was added.

**My Note:**
* Counter

Solution1:
*Time: O(n)*
*Space: O(n)*
```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d1 = collections.Counter(s)
        d2 = collections.Counter(t)
        for ch in d2:
            if ch not in d1:
                return ch
            if d2[ch] != d1[ch]:
                return ch
```
**My Note:**
* Rewrite solution1

Solution2:
*Time: O(n)*
*Space: O(n)*
```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        d1 = collections.Counter(s)
        d2 = collections.Counter(t)
        res = list((d2 - d1).keys())[0]
        return res
```

**My Note:**
* Using XOR

Solution3:
*Time: O(n)*
*Space: O(1)*
```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        i = 0
        for ch in s:
            i ^= ord(ch)
        for ch in t:
            i ^= ord(ch)
        return chr(i)
```