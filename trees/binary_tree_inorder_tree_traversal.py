from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def __init__(self):
        self.res = []

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root == None:
            return None
        
        self.inorderTraversal(root.left)
        self.res.append(root.val)
        self.inorderTraversal(root.right)

        return self.res

if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = None
    tree.right = TreeNode(2, TreeNode(3), None)

    s = Solution()
    res = s.inorderTraversal(tree)
    print(res)
