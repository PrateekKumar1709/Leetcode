import re

class Solution:
    def isNumber(self, s: str) -> bool:
        # Regular expression for a valid number
        pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$'
        return re.match(pattern, s.strip()) is not None
