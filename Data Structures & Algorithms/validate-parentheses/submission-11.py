class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
    
        for val in s:
            if val in ['{', '[', '(']:
                stack.append(val)
                continue
    
            if not stack:
                return False
    
            top = stack.pop()
    
            match top:
                case '{':
                    if val != '}':
                        return False
                case '(':
                    if val != ')':
                        return False
                case '[':
                    if val != ']':
                        return False
    
        return False if stack else True


        


            