class Solution(object):
    def sumCounts(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        j=i+1
        n=len(nums)
        sq=0
        for i in range(n):
            for j in range(i+1,n+1):
                s=set(nums[i:j])
                c=len(s)
                sq+=c*c
        return sq