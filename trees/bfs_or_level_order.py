from collections import deque

class TreeNode:
    def __init__(self, val: 'int', left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
def bfs(root: TreeNode):
    q = deque()
    q.append(root)
    
    while q:
        node = q.popleft()
        print(node.val, end=", ")
        
        if node.left:
            q.append(node.left)
        
        if node.right:
            q.append(node.right)
            
if __name__ == "__main__":
    t = TreeNode(4)
    t.left = TreeNode(2)
    t.right = TreeNode(7)
    t.left.left = TreeNode(1)
    t.left.right = TreeNode(3)
    
    t.right.right = TreeNode(9)
    t.right.left = TreeNode(6)
    
    bfs(t)
    print()