# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rightSideView(self, root):
        res = []
        queue = [[root]] if root else []
        while queue:
            layer = queue.pop(0)
            next_layer = []
            for node in layer:
                if node.left:
                    next_layer.append(node.left)
                if node.right:
                    next_layer.append(node.right)
            res.append(node.val)
            queue.append(next_layer) if next_layer else 1
        return res

test = TreeNode(1)
test.left = TreeNode(2)
test.right = TreeNode(3)
test.left.right = TreeNode(5)
test.right.right = TreeNode(4)
print(Solution().rightSideView(test))