# 510. Inorder Successor in BST II
## Medium
### Tree
#
Relative: 285
#

Given a ```node``` in a binary search tree, find the in-order successor of that node in the BST.

If that node has no in-order successor, return ```null```.

The successor of a ```node``` is the node with the smallest key greater than ```node.val```.

You will have direct access to the node but not to the root of the tree. Each node will have a reference to its parent node. Below is the definition for ```Node```:
```
class Node {
    public int val;
    public Node left;
    public Node right;
    public Node parent;
}
```

**Follow up:**

Could you solve it without looking up any of the node's values?

Example1:

![img](https://assets.leetcode.com/uploads/2019/01/23/285_example_1.PNG)
    
> Input: tree = [2,1,3], node = 1
> 
> Output: 2
>
>Explanation: 1's in-order successor node is 2. Note that both the node and the return value is of Node type.

Example2:

![img](https://assets.leetcode.com/uploads/2019/01/23/285_example_2.PNG)
    
> Input: tree = [5,3,6,2,4,null,null,1], node = 6
> 
> Output: null
>
>Explanation: There is no in-order successor of the current node, so the answer is null.

**My Note:**
* Find the root of BST
* Inorder traversal
* Get the next node

Solution1:
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        cur = node
        if not node.parent:
            root = node
        else:
            while node.parent:
                node = node.parent
            root = node
        l = []
        s = [(root, False)]
        while s:
            node, visited = s.pop()
            if node:
                if visited:
                    l.append(node)
                else:
                    s.append((node.right, False))
                    s.append((node, True))
                    s.append((node.left, False))
        idx = l.index(cur)
        if idx + 1 >= len(l):
            return 
        return l[idx + 1]
```

**My Note:**
* If right exist -> the least node in right sub-tree
* Else find the first ancestor where cur node is on its left
* Null

Solution2:
```python
"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        cur = node
        if cur.right:
            tmp = cur.right
            while tmp.left:
                tmp = tmp.left
            return tmp
        else:
            while True:
                p = cur.parent
                if not p:
                    return
                if p.left == cur:
                    return p
                if p.right == cur:
                    cur = p
```
