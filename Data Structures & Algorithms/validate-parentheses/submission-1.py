class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        matches = {")" : "(", "]" : "[","}" : "{"}

        for e in s:
            if e in matches:
                if not stack or stack[-1] != matches[e]:
                    return False
                stack.pop() 
            else:
                stack.append(e)
        
        if not stack:
            return True
        
        return False