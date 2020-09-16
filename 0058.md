# 58. Length of Last Word
## Easy
### String
#

Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word (last word means the last appearing word if we loop from left to right) in the string.

If the last word does not exist, return 0.

**Note:** 
A word is defined as a **maximal substring** consisting of non-space characters only.

Example:
> Input: "Hello World"
> 
> Output: 5

**My Note:**
* Python
* string.strip()
* string.lstrip()
* string.rstrip()

Solution:
```python
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        # print(s)
        if not s:
            return 0
        word = s.split()
        return len(word[-1])
```
