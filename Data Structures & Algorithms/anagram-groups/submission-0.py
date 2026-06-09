from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        result = defaultdict(list)

        for word in strs:
            sorted_keys = "".join(sorted(word))
            result[sorted_keys].append(word)
        return list(result.values())
