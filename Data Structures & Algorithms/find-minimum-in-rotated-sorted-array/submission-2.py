class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        
        min_ele = (2**31) - 1

        while l<=r:
            
            #already sorted array
            if nums[l]<nums[r]:
                min_ele = min(min_ele,nums[l])

            m = l+(r-l)//2

            # left side sorted
            if nums[l]<=nums[m]:
                min_ele = min(min_ele,nums[l])
                l = m+1
            
            else:
                min_ele = min(min_ele,nums[m])
                r = m-1

        
        return min_ele

            


        