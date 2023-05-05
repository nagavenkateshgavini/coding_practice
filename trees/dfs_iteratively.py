from collections import deque

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def dfs_preorder(root, res):
    stack = deque()
    
    stack.append(root)
    while stack:
        node = stack.pop()
        
        res.append(f"{node.val}")
        if node.right:
            stack.append(node.right)
        
        if node.left:
            stack.append(node.left)
            
def dfs_inorder(root, res):
    pass


def main():
    t = TreeNode(4)
    t.left = TreeNode(2)
    t.right = TreeNode(7)
    t.left.left = TreeNode(1)
    t.left.right = TreeNode(3)
    
    t.right.right = TreeNode(9)
    t.right.left = TreeNode(6)
    
    res = []
    dfs_preorder(t, res)
    print(", ".join(res))
    
if __name__ == "__main__":
    main()
