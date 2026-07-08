class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        left=0
        right=len(height)-1
        max_water=0
        while left<right:
            width=right-left
            h=min(height[left],height[right])
            are=h*width
            if are>max_water:
                max_water=are
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
        return max_water