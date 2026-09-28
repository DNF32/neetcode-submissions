class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = len(temperatures) * [0]
        
        for i in reversed(range(len(temperatures))):
            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            if stack:
                result[i] = stack[-1] -i 

            stack.append(i)
        return result


        