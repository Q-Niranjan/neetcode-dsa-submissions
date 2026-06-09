class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i,_ in enumerate(nums):
            diff = target-nums[i]
            x = hashmap.get(diff,-1)
            if x!=-1 :
                first_index = hashmap.get(diff,0)
                return [first_index,i]
            else:
                hashmap[nums[i]] = i
        
        return [0,0]