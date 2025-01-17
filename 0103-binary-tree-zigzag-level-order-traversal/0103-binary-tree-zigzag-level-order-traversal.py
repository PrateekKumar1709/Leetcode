# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        dq = deque()
        dq.append(root)
        final_res = []
        cntr = 0

        while dq:
            res = []
            cntr +=1
            for i in range(len(dq)):
                node = dq.popleft()
                res.append(node.val)

                if node.left:
                    dq.append(node.left)
                if node.right:
                    dq.append(node.right)

            if cntr % 2 == 0:
                final_res.append(res[::-1])
            else: 
                final_res.append(res)

        return final_res


