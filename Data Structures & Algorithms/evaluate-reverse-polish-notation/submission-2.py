class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for tok in tokens:
            try:
                stack.append(int(tok))
                continue
            except:
                pass

            second = stack.pop(-1)
            first = stack.pop(-1)
            if tok == "*":
                stack.append(first* second)
            elif tok == "/":
                stack.append(int(first/ second))
            elif tok == "-":
                stack.append(first- second)
            elif tok == "+":
                stack.append(first+ second)
        return stack.pop(-1)
                
                
        