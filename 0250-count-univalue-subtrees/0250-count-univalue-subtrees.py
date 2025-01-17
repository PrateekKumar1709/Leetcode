# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.count = 0
        
        def isUnivalTree(node, parent_value):
            if not node:
                return True
            
            # Check if left and right subtrees are univalue
            left_unival = isUnivalTree(node.left, node.val)
            right_unival = isUnivalTree(node.right, node.val)
            
            # If both left and right are univalue and match the current node's value
            if left_unival and right_unival:
                self.count += 1
                return node.val == parent_value
            
            return False
        
        isUnivalTree(root, None)
        return self.count
