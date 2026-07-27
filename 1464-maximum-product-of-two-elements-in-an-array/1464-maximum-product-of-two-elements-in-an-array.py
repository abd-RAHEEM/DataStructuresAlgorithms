class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort(reverse=True)
        x=nums[0]
        y=nums[1]
        return (x-1)*(y-1)