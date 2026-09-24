class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        tempAmount = len(temperatures)
        stack = []
        results = tempAmount*[0]

        for i in range(tempAmount):
            currentVal = temperatures[tempAmount-1-i]
            while len(stack) > 0:
                top = stack[-1]
                if top[0] > currentVal:
                    stack.append((currentVal,tempAmount-1-i))
                    results[tempAmount-1-i] = top[1] - (tempAmount-1-i)
                    break
                else:
                    stack.pop(-1)
            else:
                stack.append((currentVal,tempAmount-1-i))
                results[tempAmount-1-i] = 0
        return results

            


            
            
        