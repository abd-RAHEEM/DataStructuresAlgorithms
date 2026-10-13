class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in range(len(nums)):
            nums[i]=nums[i]*nums[i]
        nums.sort()
        s=0
        n=len(nums)
        for i in range(n):
            if i<(n//2):
                s-=nums[i]
            else:
                s+=nums[i]
        return s        