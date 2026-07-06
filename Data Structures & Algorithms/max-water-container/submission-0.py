class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        # container_water = 0 
        # for i , _ in enumerate(height):
        #     for j ,_ in enumerate(height[i+1:], start=i+1):
        #         h = height[i] if height[i]<=height[j] else height[j]
        #         w = j-i

        #         container_water = max(container_water,h*w)

        # return container_water

        l = 0 
        r = len(height)-1
        max_water = 0
        while l<r:
            h = min(height[l],height[r])
            w = r-l
            max_water = max(max_water, w*h)
            if height[l]<=height[r]:
                l = l+1
            else:
                r=r-1

        return max_water



 