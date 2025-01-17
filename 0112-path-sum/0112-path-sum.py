# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        curSum=0

        def calcSum(curSum, root):
            if not root:
                return False
            curSum += root.val
            if curSum == targetSum and not root.left and not root.right:
                return True
            return calcSum(curSum, root.left) or calcSum(curSum, root.right)
        return calcSum(curSum, root)
        








        