class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        # Map each closing bracket to its corresponding opening bracket
        mapping = {")": "(", "}": "{", "]": "["}
        
        for char in s:
            if char in mapping:
                # Pop the top element from stack if it's not empty, else use a dummy value
                top_element = stack.pop() if stack else '#'
                
                # If the popped opening bracket doesn't match the expected one
                if mapping[char] != top_element:
                    return False
            else:
                # If it's an opening bracket, push it to the stack
                stack.append(char)
                
        # If the stack is empty, all brackets were matched correctly
        return not stack