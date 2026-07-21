class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s=set(nums)
        n=len(nums)+1
        i=1
        while i<=n:
            if i not in s:
                return i
            i+=1
        return 1
