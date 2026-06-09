class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        
        freq = {}

        for sch,tch in zip(s,t):
            freq[sch] = freq.get(sch,0)+1
            freq[tch] = freq.get(tch,0)-1
        
        return all(count==0 for count in freq.values())
        