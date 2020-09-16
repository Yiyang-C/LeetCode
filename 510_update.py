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