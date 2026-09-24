class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        initRight = len(nums) *[1]
        initLeft = len(nums) *[1]

        for i in range(1,len(nums)):
            initRight[i] = initRight[i-1] * nums[i-1]
            initLeft[len(nums)-i-1] = initLeft[len(nums)-i] * nums[len(nums)-i]
        
        for i in range(len(nums)):
            initRight[i] = initRight[i] * initLeft[i]
            
        return initRight
        