class Solution:
    def calculate(self, s: str) -> int:
        # Initialize stack to store numbers and current number
        stack = []
        curr_num = 0
        curr_op = '+'  # Start with + to handle first number
        
        # Process each character in the string
        for i, char in enumerate(s):
            # If character is digit, build the number
            if char.isdigit():
                curr_num = curr_num * 10 + int(char)
                
            # If character is operator or last character, process the operation
            if (not char.isdigit() and char != ' ') or i == len(s) - 1:
                # Handle previous operator
                if curr_op == '+':
                    stack.append(curr_num)
                elif curr_op == '-':
                    stack.append(-curr_num)
                elif curr_op == '*':
                    stack.append(stack.pop() * curr_num)
                elif curr_op == '/':
                    # Handle division considering negative numbers
                    prev_num = stack.pop()
                    # Integer division truncating toward zero
                    if prev_num < 0:
                        stack.append(-(abs(prev_num) // curr_num))
                    else:
                        stack.append(prev_num // curr_num)
                
                # Reset current number and update operator
                curr_num = 0
                curr_op = char
        
        # Sum up all numbers in stack
        return sum(stack)