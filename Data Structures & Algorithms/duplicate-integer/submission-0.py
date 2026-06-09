class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        for i,e in enumerate(nums):
            if i<len(nums)-1  and e == nums[i+1]:
                return True 
        return False
        