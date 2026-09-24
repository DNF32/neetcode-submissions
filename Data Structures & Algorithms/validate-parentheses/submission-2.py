class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] 
        for char in s:
            if char in ["{","(","["]:
                stack.append(char)
            else:
                if not stack:
                    return False
                lachart = stack.pop(-1)
                if char =="}":
                    if lachart != "{":
                        return False
                elif char =="]":
                    if lachart != "[":
                        return False
                elif char ==")":
                    if lachart != "(":
                        return False
        return not stack
                    