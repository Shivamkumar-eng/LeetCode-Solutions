class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                right = stack.pop()
                left = stack.pop()
                stack.append(left - right)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                right = stack.pop()
                left = stack.pop()
                # int() truncates towards zero in Python, matching requirements
                stack.append(int(left / right))
            else:
                stack.append(int(token))
                
        return stack[0]