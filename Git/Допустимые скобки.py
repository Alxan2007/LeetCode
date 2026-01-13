class Solution:
    def isValid(self, s: str) -> bool:
            stack = []
            parenthesis= {'(': ')', '{': '}', '[': ']'}
            for i in s:
                if i in parenthesis:
                    stack.append(i)
                elif len(stack) == 0 or parenthesis[stack.pop()] != i:
                    return False
            return stack == []