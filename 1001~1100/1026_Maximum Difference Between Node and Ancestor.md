# 1026. Maximum Difference Between Node and Ancestor
## Medium
### Tree/Depth-first Search
#

Given the ```root``` of a binary tree, find the maximum value ```V``` for which there exist **different** nodes ```A``` and ```B``` where ```V = |A.val - B.val|``` and ```A``` is an ancestor of ```B```.

A node ```A``` is an ancestor of ```B``` if either: any child of ```A``` is equal to ```B```, or any child of ```A``` is an ancestor of ```B```.

Example1:

![img1](https://assets.leetcode.com/uploads/2020/11/09/tmp-tree.jpg)
> Input: root = [8,3,10,1,6,null,14,null,null,4,7,13]
> 
> Output: 7
>
> Explanation: We have various ancestor-node differences, some of which are given below :
>
> |8 - 3| = 5
>
> |3 - 7| = 4
>
> |8 - 1| = 7
>
> |10 - 13| = 3
>
> Among all possible differences, the maximum value of 7 is obtained by |8 - 1| = 7.

Example2:

![img2](https://assets.leetcode.com/uploads/2020/11/09/tmp-tree-1.jpg)
> Input: root = [1,null,2,null,0,3]
> 
> Output: 3

**Constraints:** 
* The number of nodes in the tree is in the range ```[2, 5000]```.
* ```0 <= Node.val <= 10^5```

**My Note:**
* DFS each node to return the max and min value of its children and itself recursively
* When the node is not a leaf node calculate and compare to the ```self.res```

Solution1:
*Time: O(n)*
*Space: O(1)*
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node) -> List[int]:
            if not node.left and not node.right:
                return node.val, node.val
            if not node.left:
                r = dfs(node.right)
                self.res = max(self.res, abs(node.val - r[0]), abs(node.val - r[1]))
                return min(node.val, r[0]), max(node.val, r[1])
            if not node.right:
                l = dfs(node.left)
                self.res = max(self.res, abs(node.val - l[0]), abs(node.val - l[1]))
                return min(node.val, l[0]), max(node.val, l[1])
            l,r = dfs(node.left), dfs(node.right)
            self.res = max(self.res, abs(node.val - l[0]), abs(node.val - l[1]), abs(node.val - r[0]), abs(node.val - r[1]))
            return min(node.val, l[0], r[0]), max(node.val, l[1], r[1])
            
        dfs(root)
        return self.res
```
