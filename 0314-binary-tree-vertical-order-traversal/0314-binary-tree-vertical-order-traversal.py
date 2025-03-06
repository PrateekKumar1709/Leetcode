from collections import defaultdict, deque
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        column_map = defaultdict(list)
        queue = deque([(root, 0)])  # (node, column)
        min_column = max_column = 0
        
        while queue:
            node, column = queue.popleft()
            column_map[column].append(node.val)
            
            min_column = min(min_column, column)
            max_column = max(max_column, column)
            
            if node.left:
                queue.append((node.left, column - 1))
            if node.right:
                queue.append((node.right, column + 1))
        
        return [column_map[col] for col in range(min_column, max_column + 1)]
