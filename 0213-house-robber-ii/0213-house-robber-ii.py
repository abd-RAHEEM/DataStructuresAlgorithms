class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob1=0
        rob2=0
        if len(nums)==1:
            return nums[0]
        for i in range(len(nums)-1):
            temp=max(nums[i]+rob1,rob2)
            rob1=rob2
            rob2=temp
        rob3=0
        rob4=0
        for i in range(1,len(nums)):
            temp=max(nums[i]+rob3,rob4)
            rob3=rob4
            rob4=temp
        return max(rob2, rob4)