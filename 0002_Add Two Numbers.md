# 2. Add Two Numbers
## Medium
### Linked List/Math
#
Relative: 43, 67, 371, 415, 445, 989
#

You are given two **non-empty** linked lists representing two non-negative integers. The digits are stored in **reverse order** and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:
> Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
> 
> Output: 7 -> 0 -> 8
>
> Explanation: 342 + 465 = 807.

**My Note:**
* Convert to strings
* Reverse both strings
* Add them up then store the result in linked list

Solution1:
*Time: O(n)*
*Space: O(n)*
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = '', ''
        while l1:
            s1 += str(l1.val)
            l1 = l1.next
        while l2:
            s2 += str(l2.val)
            l2 = l2.next
        res = int(s1[::-1]) + int(s2[::-1])
        s = str(res)[::-1]
        ret = cur = ListNode(0)
        for ch in s:
            cur.next = ListNode(int(ch))
            cur = cur.next
        return ret.next
```
