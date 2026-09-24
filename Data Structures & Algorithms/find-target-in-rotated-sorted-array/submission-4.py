class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0 
        right = len(nums) -1

        while left <= right:
            mid = (left + right)//2
            midValue = nums[mid]
            leftValue = nums[left]
            rightValue = nums[right]

            if midValue == target:
                return mid

            if leftValue <= midValue:
                if leftValue <=target<midValue:
                    right = mid -1
                else:
                    left = mid + 1
            else:
                if midValue < target <= rightValue:
                    left = mid + 1
                else:
                    right = mid -1

        return -1


         