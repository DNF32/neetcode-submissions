
from typing import List
from dataclasses import dataclass

@dataclass
class Chain:
    left: int
    right: int


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        chains = []
        unique = list(set(nums))

        for num in unique:
            indexSeq = []

            for i, chain in enumerate(chains):
                if num == chain.left - 1:
                    chain.left = num
                    indexSeq.append(i)

                elif num == chain.right + 1:
                    chain.right = num
                    indexSeq.append(i)

            if len(indexSeq) == 2:
                i, j = indexSeq
                chains[i].left = min(chains[i].left, chains[j].left)
                chains[i].right = max(chains[i].right, chains[j].right)
                chains.pop(j)
                
            elif len(indexSeq) == 0:
                chains.append(Chain(num, num))

        if not chains:
            return 0

        return max(chain.right - chain.left + 1 for chain in chains) 