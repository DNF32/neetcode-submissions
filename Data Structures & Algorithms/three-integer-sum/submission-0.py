class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        allTriplets = []
        nums.sort()
        for i in range(len(nums)): 
            target = -nums[i]
            subArray = nums[0:i] + nums[i+1:-1]
            solution = self.twoSum(subArray, target)

            if solution:
                allTriplets.extend(solution)
        
        unique = set()

        for triplet in allTriplets:
            unique.add(tuple(sorted(triplet)))
        
        return [list(t) for t in unique] 




    def twoSum(self, nums, target):
        left = 0
        right = len(nums) -1
        sol = []

        while left < right :
            total = nums[left] + nums[right]
            if total == target:
                sol.append([nums[left], nums[right],-target])
                while left < right and nums[left] == nums[left+1]:
                    left +=1
                while left < right and nums[right] == nums[right-1]:
                    right -=1

                left += 1
                right -= 1

            elif total < target:
                left +=1
            else:
                right-= 1
        return sol
            


        