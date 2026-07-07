class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # for i in range(len(nums)):
        #     if target == nums[i]:
        #         index = i
        #         break
        
        # return index

        l = 0
        r = len(nums)-1

        while l<=r:
            m = l+(r-l)//2

            if target==nums[m]:
                return m;
            
            if nums[l]<=nums[m]:
                # search in left half
                if nums[l]<=target and target<nums[m]:
                    r = m-1
                else:
                    l = m+1
            else:
                # search in right half
                if nums[m]< target and target<=nums[r]:
                    l = m+1
                else:
                    r = m-1
           
        return -1



        