from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        pairs = {
            ')':'(',
            '}':'{',
            ']':'['
        }
        stack = deque()
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            else:
                if not stack or stack[-1]!=pairs[ch]:
                    return False
                stack.pop()
        
        return not stack

        