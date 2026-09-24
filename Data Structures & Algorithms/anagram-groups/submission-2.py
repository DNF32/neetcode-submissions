class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}

        for val in strs:
            unique = "".join(sorted(val))
            if unique in anagrams:
                anagrams[unique].append(val)
            else:
                anagrams[unique] = [val]
        
        return [value for (key,value) in anagrams.items()]

        