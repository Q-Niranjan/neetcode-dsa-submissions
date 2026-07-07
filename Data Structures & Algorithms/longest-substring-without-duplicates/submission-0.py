class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        freq = {}
        ans = 0
        left = 0
        for right in range(len(s)):
            freq[s[right]] = freq.get(s[right],0)+1

            while freq.get(s[right],0)>1:
                freq[s[left]] = freq.get(s[left],0)-1
                left = left+1

            ans = max(ans,right-left+1)
            
        return ans
        
        

           



        