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
            if op in {'+', '-'}:
                return 1
            if op in {'*', '/'}:
                return 2
            return 0  # For '('
        
        # Initialize stacks for numbers and operators
        num_stack = []
        op_stack = []
        
        i = 0
        while i < len(s):
            if s[i].isspace():
                i += 1
                continue
            
            if s[i].isdigit():
                # Accumulate digits to form a number
                num = 0
                while i < len(s) and s[i].isdigit():
                    num = num * 10 + int(s[i])
                    i += 1
                num_stack.append(num)
                continue
            
            if s[i] in {'+', '-', '*', '/'}:
                # Process operators based on precedence
                while op_stack and precedence(op_stack[-1]) >= precedence(s[i]):
                    num_stack.append(apply_op(op_stack.pop(), num_stack.pop(), num_stack.pop()))
                op_stack.append(s[i])
            
            i += 1
        
        # Process any remaining operators
        while op_stack:
            num_stack.append(apply_op(op_stack.pop(), num_stack.pop(), num_stack.pop()))
        
        # The final result is the only item left in the number stack
        return num_stack[0]

# Test cases
solution = Solution()
test_cases = [
    "3+2*2",
    " 3/2 ",
    " 3+5 / 2 ",
    "1-1+1",
    "10+2*3+4*5",
    "2-3+4",
    " 0 ",
    "1+1-1",
    "2*3-4*5"
]

for test in test_cases:
    print(f"Input: {test}")
    print(f"Output: {solution.calculate(test)}")
    print()
