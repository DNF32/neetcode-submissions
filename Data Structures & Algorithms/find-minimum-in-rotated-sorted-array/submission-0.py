class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) -1
        minVal = 1001
        
        while left<= right:
            mid = (left + right) //2

            if nums[mid] <= nums[right]:
                minVal = min(minVal, nums[mid])
                right = mid-1
            else:
                minVal = min(minVal,nums[left])
                left = mid+1

        return minVal

