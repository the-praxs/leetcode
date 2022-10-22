class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # Stack to maintain becaket order
        brackets = {')': '(', '}':'{' ,']':'['} # HashMap of Brackets

        for char in s:
            # If bracket is closing bracket
            if char in brackets:
                # Check if stack is not empty and top of stack is opening bracket
                if stack and stack[-1] == brackets[char]:
                    stack.pop()
                else: # Stack is empty hence invalid
                    return False
            else:
                stack.append(char)

        return not stack