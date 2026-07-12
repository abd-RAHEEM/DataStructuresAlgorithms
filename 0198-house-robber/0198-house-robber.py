class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob1=0
        rob2=0
        #  [rob1, rob2, num, num+!,....
        for num in nums:
            temp=max(rob1+num,rob2)
            rob1=rob2
            rob2=temp
        return rob2