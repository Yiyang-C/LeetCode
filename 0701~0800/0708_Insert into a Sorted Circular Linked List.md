# 708. Insert into a Sorted Circular Linked List
## Medium
### Linked List
#
Relative: 147
#

Given a node from a **Circular Linked List** which is sorted in ascending order, write a function to insert a value ```insertVal``` into the list such that it remains a sorted circular list. The given node can be a reference to any single node in the list, and may not be necessarily the smallest value in the circular list.

If there are multiple suitable places for insertion, you may choose any place to insert the new value. After the insertion, the circular list should remain sorted.

If the list is empty (i.e., given node is ```null```), you should create a new single circular list and return the reference to that single node. Otherwise, you should return the original given node.

Example1:

![](https://assets.leetcode.com/uploads/2019/01/19/example_1_before_65p.jpg)
> Input: head = [3,4,1], insertVal = 2
> 
> Output: [3,4,1,2]
>
> Explanation: In the figure above, there is a sorted circular list of three elements. You are given a reference to the node with value 3, and we need to insert 2 into the list. The new node should be inserted between node 1 and node 3. After the insertion, the list should look like this, and we should still return node 3.
> 
> ![](https://assets.leetcode.com/uploads/2019/01/19/example_1_after_65p.jpg)

Example2:
> Input: head = [], insertVal = 1
> 
> Output: [1]
> 
> Explanation: The list is empty (given head is null). We create a new single circular list and return the reference to that single node.

Example3:
> Input: head = [1], insertVal = 0
> 
> Output: [1,0]

**Constraints:** 
* ```0 <= Number of Nodes <= 5 * 10^4```
* ```-10^6 <= Node.val <= 10^6```
* ```-10^6 <= insertVal <= 10^6```

**My Note:**
* [LeetCode Discuss](https://leetcode.com/problems/insert-into-a-sorted-circular-linked-list/discuss/564554/RZ-Python-one-pass-O(n)-solution-with-explanation)
* Loop the linked list to find the insert position
* Stop the while loop when cur.next == head, which would be the last position of the list 
* Case 1: insert value is within value range of the list
* Case 2: insert value is greater than max value or less than min value

Solution:
*Time: O(n)*
*Space: O(1)*
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        if not head:
            res = Node()
            res.val = insertVal
            res.next = res
            return res
        cur = head
        while cur.next != head:
            if cur.val <= insertVal <= cur.next.val:
                break
            if cur.val > cur.next.val and (insertVal > cur.val or insertVal < cur.next.val):
                break
            cur = cur.next
        ins = Node(insertVal)
        ins.next = cur.next
        cur.next = ins
        return head
```
