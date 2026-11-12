class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        leng=1
        i,j=0,1
        inc=1
        while j<len(nums):
            if nums[i]<nums[j]:
                inc+=1
                leng=max(leng,inc)
            else:
                inc=1
            i+=1
            j+=1

        lang=1
        i,j=0,1
        dec=1
        while j<len(nums):
            if nums[i]>nums[j]:
                dec+=1
                lang=max(lang,dec)
            else:
                dec=1
            i+=1
            j+=1
        return max(lang,leng)
