class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from collections import defaultdict
        freq = defaultdict(int)
        result = []
        for num in nums:
            freq[num] = freq.get(num,0) +1

        sorted_freq = dict(sorted(freq.items(),key=lambda x:x[1],reverse=True))
        
        templist = list(sorted_freq.keys())
        for item in templist:
            if k>0:
                result.append(item)
            k -=1
        return result

