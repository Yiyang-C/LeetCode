# 111. Minimum Depth of Binary Tree
## Easy
### Tree/Depth-first Search/Breadth-first Search
#
Relative: 102, 104
#

Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

**Note:**
A leaf is a node with no children.

Example1:

![img1](https://assets.leetcode.com/uploads/2020/10/12/ex_depth.jpg)
> Input: root = [3,9,20,null,null,15,7]
> 
> Output: 2

Example2:
> Input: root = [2,null,3,null,4,null,5,null,6]
> 
> Output: 5

**Constraints:** 
* The number of nodes in the tree is in the range ```[0, 10^5]```.
* ```-1000 <= Node.val <= 1000```

**My Note:**
* BFS

Solution1:
*Time: O(n)*
*Space: O(n)*
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        nodes = collections.deque()
        nodes.append((root, 1))
        while nodes:
            node, depth = nodes.popleft()
            if self.isLeaf(node):
                return depth
            if node:
                nodes.append((node.left, depth + 1))
                nodes.append((node.right, depth + 1))
        
    def isLeaf(self, node: TreeNode) -> bool:
        if not node:
            return False
        if not node.left and not node.right:
            return True
        return False
```

**My Note:**
* BFS

Solution2:
*Time: O(n)*
*Space: O(h)*
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        if not root.right:
            return self.minDepth(root.left) + 1
        if not root.left:
            return self.minDepth(root.right) + 1
        else:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
```
