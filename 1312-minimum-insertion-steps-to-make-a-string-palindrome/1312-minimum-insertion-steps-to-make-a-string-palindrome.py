class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        rs=s[::-1]
        n=len(s)
        m=n
        prev=[0]*(n+1)
        ans=0
        for i in range(1,n+1):
            cur=[0]*(n+1)
            for j in range(1,n+1):
                if s[i-1]==rs[j-1]:
                    cur[j]=1+prev[j-1]
                    ans=max(ans,cur[j])
                else:
                    cur[j]=max(prev[j],cur[j-1])
            prev=cur
        return n-prev[n]
