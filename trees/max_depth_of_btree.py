from typing import Optional
from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def _maxDepthRecursive(self, root: Optional[TreeNode]):
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def _maxDepthBFSIterative(self, root: Optional[TreeNode]):
        q = deque()
        q.append(root) # or q = deque([root])
        level = 0
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                if node.right:
                    q.append(node.right)
                if node.left:
                    q.append(node.left)
            level += 1
        return level

    def _maxDeothDFSIterative(self, root: Optional[TreeNode]):
        stack = deque()
        depth = 1
        stack.append([root, depth])
        res = 1
        while stack:
            node, depth = stack.pop()
            if node:
                res = max(res, depth)
                stack.append([node.left, depth + 1])
                stack.append([node.right, depth + 1])
        
        return res

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self._maxDeothDFSIterative(root)
        

if __name__ == "__main__":
    t = TreeNode(3)
    t.left = TreeNode(9)
    t.right = TreeNode(20)
    
    t.right.right = TreeNode(7)
    t.right.left = TreeNode(15)

    s = Solution()

    res = s.maxDepth(t)

    print(f"max depth: {res}")