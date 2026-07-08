class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left=0
        n=len(numbers)
        right=len(numbers)-1
        while left<=right:
            num=numbers[left]+numbers[right]
            if num==target:
                return [left+1,right+1]
            elif num<target:
                left+=1
            else:
                right-=1        