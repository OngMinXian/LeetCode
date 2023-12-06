# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1, root2) -> bool:
        
        self.val_1 = []
        self.val_2 = []

        def InOrderTraversal(node, n):
            # Visit left node
            if node.left != None:
                InOrderTraversal(node.left, n)

            # Visit right node
            if node.right != None:
                InOrderTraversal(node.right, n)

            # Leaf node
            if node.left == None and node.right == None:
                if n == 1:
                    self.val_1.append(node.val)
                elif n == 2:
                    self.val_2.append(node.val)

            # Return to parent
            return 

        InOrderTraversal(root1, 1)
        InOrderTraversal(root2, 2)
        return self.val_1 == self.val_2

root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)
print(Solution().leafSimilar(root, root))
