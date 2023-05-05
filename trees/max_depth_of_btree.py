# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode], res) -> int:
        pass
        

if __name__ == "__main__":
    t = TreeNode(4)
    t.left = TreeNode(2)
    t.right = TreeNode(7)
    t.left.left = TreeNode(1)
    t.left.right = TreeNode(3)
    
    t.right.right = TreeNode(9)
    t.right.left = TreeNode(6)
    s = Solution()
    res = []
    s.maxDepth(root, res)
    print(f"max depth: {res[0]}")