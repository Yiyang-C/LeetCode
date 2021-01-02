# 1379. Find a Corresponding Node of a Binary Tree in a Clone of That Tree
## Medium
### Tree/Depth-first Search/Breadth-first Search/Recursion
#

Given two binary trees ```original``` and ```cloned``` and given a reference to a node ```target``` in the original tree.

The ```cloned``` tree is a **copy of** the ```original``` tree.

Return a *reference to the same node* in the ```cloned``` tree.

**Note** that you are **not allowed** to change any of the two trees or the ```target``` node and the answer **must be** a reference to a node in the ```cloned``` tree.

**Follow up:** Solve the problem if repeated values on the tree are allowed.

**Example1:**

![img1](https://assets.leetcode.com/uploads/2020/02/21/e1.png)
> Input: tree = [7,4,3,null,null,6,19], target = 3
> 
> Output: 3
>
> Explanation:
>
> In all examples the original and cloned trees are shown. The target node is a green node from the original tree. The answer is the yellow node from the cloned tree.

**Example2:**

![img2](https://assets.leetcode.com/uploads/2020/02/21/e2.png)
> Input: tree = [7], target =  7
> 
> Output: 7

**Example3:**

![img3](https://assets.leetcode.com/uploads/2020/02/21/e3.png)
> Input: tree = [8,null,6,null,5,null,4,null,3,null,2,null,1], target = 4
> 
> Output: 4

**Example4:**

![img4](https://assets.leetcode.com/uploads/2020/02/21/e4.png)
> Input: tree = [1,2,3,4,5,6,7,8,9,10], target = 5
> 
> Output: 5

**Example5:**

![img4](https://assets.leetcode.com/uploads/2020/02/21/e5.png)
> Input: tree = [1,2,null,3], target = 2
> 
> Output: 2

**Constraints:** 
* The number of nodes in the ```tree``` is in the range ```[1, 10^4]```.
* The values of the nodes of the ```tree``` are unique.
* ```target``` node is a node from the ```original``` tree and is not ```null```.

**My Note:**
* Traverse the tree
* Find the node val equals to the val of target node

Solution:
*Time: O(n)*
*Space: O(n)*
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        q = [cloned]
        while q:
            cur = q.pop(0)
            if cur.val == target.val:
                return cur
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
```

**My Note:**
* Generator
* [LeetCode Discuss](https://leetcode.com/problems/find-a-corresponding-node-of-a-binary-tree-in-a-clone-of-that-tree/discuss/537686/Python-Clean-and-Pythonic-way-using-generator-solving-followup-too)

Follow Up Solution:
*Time: O(n)*
*Space: O(1)*
```python
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        
        def search(node):
            if node:
                yield node
                yield from search(node.left)
                yield from search(node.right)
                
        for tmp, cur in zip(search(original), search(cloned)):
            if tmp == target:
                return cur
```
