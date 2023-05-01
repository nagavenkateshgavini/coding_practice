from typing import Optional
from dfs import dfs_preorder

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    
    def _invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        
        temp = root.right
        root.right = root.left
        root.left = temp
        self._invertTree(root.left)
        self._invertTree(root.right)
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        res = []
        dfs_preorder(root, res)
        res2 = []
        self._invertTree(root)
        print(res)
        dfs_preorder(root, res2)
        print(res2)
        
if __name__ == "__main__":
    t = TreeNode(4)
    t.left = TreeNode(2)
    t.right = TreeNode(7)
    t.left.left = TreeNode(1)
    t.left.right = TreeNode(3)
    
    t.right.right = TreeNode(9)
    t.right.left = TreeNode(6)
    
    s= Solution()
    s.invertTree(t)
    