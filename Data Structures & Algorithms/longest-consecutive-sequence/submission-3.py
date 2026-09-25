class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        unique = set(nums)
        longest = 0

        for num in unique:
            if num -1 not in unique:
                lenght = 1

                while num + lenght in unique:
                    lenght +=1

                longest = max(longest, lenght)
        return longest





            
                    
