class Solution(object):
    def findTargetSumWays(self, nums, target):
        total=sum(nums)
        if abs(target)>total or (total+target)%2!=0:
            return 0
        s=(total+target)//2
        dp=[0]*(s+1)
        dp[0]=1

        for num in nums:
            for i in range(s,num-1,-1):
                dp[i]+=dp[i-num]
        return dp[s]