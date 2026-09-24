class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1

        keys_list = list(counts.keys())
        final = self.kthLargest(keys_list,counts,0,len(keys_list)-1,k,[])
        return final


    def partition(self,keys,counts,l,r): 
        pivot = counts[keys[r]]
        i=l
        for j in range(l,r):
            if counts[keys[j]] <= pivot:
                keys[j], keys[i] = keys[i], keys[j]
                i +=1

        keys[r], keys[i] = keys[i], keys[r]
        return i

    def kthLargest(self,keys,counts, l, r, k, total):
        if k> 0 and k <= r- l +1:
            index = self.partition(keys,counts,l,r)

            if index == r -k + 1:
                total.extend(keys[index:r+1])
                return total
            
            if index < r-k+ 1:
                return self.kthLargest(keys,counts, index+1, r,k,  total)
            
            total.extend(keys[index:r+1])
            return self.kthLargest(keys, counts, l, index-1,k - (r-index+1) , total)
        return total
        