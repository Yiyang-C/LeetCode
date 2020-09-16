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
        