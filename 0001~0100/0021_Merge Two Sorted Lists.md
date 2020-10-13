# 21. Merge Two Sorted Lists
## Easy
### Linked List
#
Relative: 23, 88, 148, 244
#

Merge two sorted linked lists and return it as a new **sorted** list. The new list should be made by splicing together the nodes of the first two lists.

Example1:

![img](https://assets.leetcode.com/uploads/2020/10/03/merge_ex1.jpg)

> Input: l1 = [1,2,4], l2 = [1,3,4]
> 
> Output: [1,1,2,3,4,4]

Example2:
> Input: l1 = [], l2 = []
> 
> Output: []

Example3:
> Input: l1 = [], l2 = [0]
> 
> Output: [0]

**Constraints:** 
* The number of nodes in both lists is in the range ```[0, 50]```.
* ```-100 <= Node.val <= 100```
* Both ```l1``` and ```l2``` are sorted in **non-decreasing** order.

**My Note:**
* Simple Linked List Question

Solution:
*Time: O(n)*
*Space: O(1)*
```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ret = res = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                res.next = l1
                res = res.next
                l1 = l1.next
            else:
                res.next = l2
                res = res.next
                l2 = l2.next
        if l1:
            res.next = l1
        if l2:
            res.next = l2
        return ret.next
```
