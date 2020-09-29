# 139. Word Break
## Medium
### Dynamic Programming
#
Relative: 140
#

Given a **non-empty** string s and a dictionary wordDict containing a list of **non-empty** words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

**Note:** 
* The same word in the dictionary may be reused multiple times in the segmentation.
* You may assume the dictionary does not contain duplicate words.

Example1:
> Input: s = "leetcode", wordDict = ["leet", "code"]
> 
> Output: true
>
> Explanation: Return true because "leetcode" can be segmented as "leet code".

Example2:
> Input: s = "applepenapple", wordDict = ["apple", "pen"]
> 
> Output: true
>
> Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
>
> Note that you are allowed to reuse a dictionary word.

Example3:
> Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
> 
> Output: false

**My Note:**
* Typical DP

Solution1:
*Time: O(n^2)*
*Space: O(n)*
```python
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        dp = [False for _ in range(len(s))]
        for i in range(len(s)):
            if s[:i+1] in wordSet:
                dp[i] = True
            else:
                for j in range(i):
                    if dp[j] and s[j+1:i+1] in wordSet:
                        dp[i] = True
                        break
        return dp[-1]
```
