class Solution:
    def threeSum(sekf, nums: List[int]) -> List[List[int]]:
        res = []

        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left = i+ 1
            right = len(nums)-1
            target = -nums[i]

            while left< right:
                leftV = nums[left]
                rightV = nums[right]
    
                s = leftV + rightV
    
                if s > target:
                    right -=1
                elif s< target:
                    left +=1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    while left < right and nums[left+1] == nums[left]:
                            left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1

                    left +=1
                    right -=1
        return res

            
        
