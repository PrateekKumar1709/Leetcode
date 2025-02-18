class Solution:
    def calculate(self, s: str) -> int:
        # Helper function to perform arithmetic operations
        def apply_op(op, b, a):
            if op == '+': return a + b
            if op == '-': return a - b
            if op == '*': return a * b
            if op == '/': return int(a / b)  # Integer division truncating toward zero
        
        # Helper function to get operator precedence
        def precedence(op):
            if op in {'+', '-'}: return 1
            if op in {'*', '/'}: return 2
            return 0
        
        # Remove whitespace from input string
        s = s.replace(" ", "")
        
        # Initialize stacks for numbers and operators
        nums = []
        ops = []
        i = 0
        
        while i < len(s):
            char = s[i]
            
            # If current character is a digit
            if char.isdigit():
                # Parse multi-digit number
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                nums.append(num)
                continue
                
            # If current character is an operator
            if char in {'+', '-', '*', '/'}:
                # Process operators with higher or equal precedence
                while (ops and precedence(ops[-1]) >= precedence(char)):
                    nums.append(apply_op(ops.pop(), nums.pop(), nums.pop()))
                ops.append(char)
                
            i += 1
        
        # Process remaining operators
        while ops:
            nums.append(apply_op(ops.pop(), nums.pop(), nums.pop()))
        
        return nums[0]

            