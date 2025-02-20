# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # Initialize global maximum with smallest possible value
        self.max_sum = float('-inf')
        
        def max_gain(node):
            if not node:
                return 0
            
            # Recursively compute maximum path sum for left and right subtrees
            # Take max of 0 and path sum to handle negative values
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)
            
            # Current path sum including current node and both children
            current_path_sum = node.val + left_gain + right_gain
            
            # Update global maximum if current path sum is larger
            self.max_sum = max(self.max_sum, current_path_sum)
            
            # Return maximum single path (including at most one child)
            # This value will be used by parent nodes
            return node.val + max(left_gain, right_gain)
        
        max_gain(root)
        return self.max_sum
