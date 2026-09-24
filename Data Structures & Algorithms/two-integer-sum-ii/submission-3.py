class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while left < right:
            total = numbers[left] + numbers[right]
            if total > target:
                currentRight = numbers[right]
                right -= 1
                while left < right and numbers[right] == currentRight:
                    right -=1
            elif total < target:
                currentLeft= numbers[left]
                left += 1
                while left < right and numbers[left] == currentLeft:
                    left +=1
            else:
                return [left +1, right +1]

                     
