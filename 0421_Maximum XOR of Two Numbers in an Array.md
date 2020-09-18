# 421. Maximum XOR of Two Numbers in an Array
## Medium
### Bit Manipulation/Trie
#

Given a **non-empty** array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.

Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?

Example:
>Input: [3, 10, 5, 25, 2, 8]
>
>Output: 28
>
>Explanation: The maximum result is 5 ^ 25 = 28.

**My Note:**
* Using Trie structure to store binary digit of each num
* Traverse all the num find the res
* string.zfill(n) # add heading 0's to make len(string) = n

Solution1:
*Time: O(n)*
*Space: O(n)*
```python
class TrieNode:
    def __init__(self):
        self.child = {}
        self.end = False
    
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        trie = Trie()
        max_len = len(bin(max(nums))) - 2
        for num in nums:
            tmp = bin(num).split('0b')[1].zfill(max_len)
            # print(tmp)
            root = trie.root
            for ch in tmp:
                root = root.child.setdefault(ch, TrieNode())
            root.end = True
        # print(trie.root.child['0'].child)

        res = 0
        for num in nums:
            tmp = bin(num).split('0b')[1].zfill(max_len)
            root = trie.root
            pair = ''
            for ch in tmp:
                if ch == '1':
                    if '0' not in root.child:
                        pair += '1'
                        root = root.child['1']
                    else:
                        pair += '0'
                        root = root.child['0']
                else:
                    if '1' not in root.child:
                        pair += '0'
                        root = root.child['0']
                    else:
                        pair += '1'
                        root = root.child['1']
            res = max(res, num ^ int(pair, 2))
        return res
```

**My Note:**
* https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/discuss/849128/Python-O(32n)-solution-explained

Solution2:
*Time: O(n)*
*Space: O(n)*
```python
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res = mask = 0
        for i in range(32)[::-1]:
            mask |= 1 << i
            s = set()
            for num in nums:
                s.add(num & mask)
            start = res | 1 << i
            for tmp in s:
                if start ^ tmp in s:
                    res = start
                    break
        return res
```

Brute Force Solution: (TLE)
```python
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        res = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                res = max(res, nums[i] ^ nums[j])
        return res
```
