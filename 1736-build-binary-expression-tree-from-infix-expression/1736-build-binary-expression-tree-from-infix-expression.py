class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def expTree(self, s: str) -> 'Node':
        def precedence(op):
            if op in ('+', '-'):
                return 1
            if op in ('*', '/'):
                return 2
            return 0

        def apply_operator(operators, nodes):
            operator = operators.pop()
            right = nodes.pop()
            left = nodes.pop()
            nodes.append(Node(operator, left, right))

        operators = []
        nodes = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                nodes.append(Node(s[i]))
            elif s[i] == '(':
                operators.append(s[i])
            elif s[i] == ')':
                while operators and operators[-1] != '(':
                    apply_operator(operators, nodes)
                operators.pop()  # pop '('
            else:  # operator
                while (operators and operators[-1] != '(' and
                       precedence(operators[-1]) >= precedence(s[i])):
                    apply_operator(operators, nodes)
                operators.append(s[i])
            i += 1

        while operators:
            apply_operator(operators, nodes)

        return nodes[0]

# Example usage:
# sol = Solution()
# root = sol.expTree("3+4*2-5")
