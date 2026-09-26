class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1

        while left< right:
            leftV = numbers[left]
            rightV = numbers[right]

            s = leftV + rightV

            if s > target:
                right -=1
            elif s< target:
                left +=1
            else:
                return [left +1, right+1]
        