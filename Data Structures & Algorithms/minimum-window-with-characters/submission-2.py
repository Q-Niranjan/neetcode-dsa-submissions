class Solution:
    def minWindow(self, s: str, t: str) -> str:

        t_freq = {}
        for ch in t:
            t_freq[ch] = t_freq.get(ch,0)+1

        window_freq = {}

        have, need = 0, len(t_freq)

        res, res_len = [-1, -1], float("inf")
        left = 0
        for right in range(len(s)):
            ch = s[right]
            window_freq[ch] = window_freq.get(ch, 0) + 1

            if ch in t_freq and window_freq[ch] == t_freq[ch]:
                have += 1

            while have == need:
                if (right - left + 1) < res_len:
                    res = [left, right]
                    res_len = right - left + 1

                left_ch = s[left]
                window_freq[left_ch] -= 1

                if left_ch in t_freq and window_freq[left_ch] < t_freq[left_ch]:
                    have -= 1
                
                left += 1
        
        left, right = res
        return s[left : right + 1] if res_len != float("inf") else ""











                

        