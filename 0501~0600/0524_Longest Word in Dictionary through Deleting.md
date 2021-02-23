# 524. Longest Word in Dictionary through Deleting
## Medium
### Two Pointers/Sort
#
Relative: 720
#

Given a string and a string dictionary, find the longest string in the dictionary that can be formed by deleting some characters of the given string. If there are more than one possible results, return the longest word with the smallest lexicographical order. If there is no possible result, return the empty string.

Example1:
> Input: s = "abpcplea", d = ["ale","apple","monkey","plea"]
> 
> Output: "apple"

Example2:
> Input: s = "abpcplea", d = ["a","b","c"]
> 
> Output: "a"

**Note:** 
* All the strings in the input will only contain lower-case letters.
* The size of the dictionary won't exceed 1,000.
* The length of all the strings in the input won't exceed 1,000.

**My Note:**
* Sort the dictionary (List[str])
* Compare two Stings using two pointers

Solution1:
*Time: O(nm)*
*Space: O(n)*
```python
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        d = sorted(d)
        d = sorted(d, key=lambda x: len(x), reverse=True)
        for cur_s in d:
            i = j = 0
            while i < len(s) and j < len(cur_s):
                if s[i] == cur_s[j]:
                    if j == len(cur_s)-1:
                        return cur_s
                    i += 1
                    j += 1
                else:
                    i += 1
        return ""
```
