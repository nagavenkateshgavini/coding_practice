class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def dfs_preorder(root: TreeNode, res: "List"):
    if not root:
        return None
    res.append(f"{root.val} ")
    dfs_preorder(root.left, res)
    dfs_preorder(root.right, res)
    
def dfs_inorder(root: TreeNode, res: "List"):
    if not root:
        return None
    dfs_inorder(root.left, res)
    res.append(f"{root.val} ")
    dfs_inorder(root.right, res)
    
def dfs_postorder(root: TreeNode, res: "List"):
    if not root:
        return None
    dfs_postorder(root.left, res)
    dfs_postorder(root.right, res)
    res.append(f"{root.val} ")


def main():
    t = TreeNode(4)
    t.left = TreeNode(2)
    t.right = TreeNode(7)
    t.left.left = TreeNode(1)
    t.left.right = TreeNode(3)
    
    t.right.right = TreeNode(9)
    t.right.left = TreeNode(6)
    
    result = []
    dfs_postorder(t, result)
    print("".join(result))
    
if __name__ == "__main__":
    main()
