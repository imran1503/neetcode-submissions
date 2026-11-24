class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matching = {')': '(', '}': '{', ']': '['}

        for c in s:
            if c in '({[':                 
                stack.append(c)
            else:                          
                if not stack:
                    return False           
                if stack.pop() != matching[c]:
                    return False           
        return not stack                   
        