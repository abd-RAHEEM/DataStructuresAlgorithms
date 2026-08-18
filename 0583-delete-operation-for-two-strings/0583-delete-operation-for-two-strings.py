class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        n=len(word1)
        m=len(word2)
        prev=[0]*(m+1)
        for i in range(1,n+1):
            cur=[0]*(m+1)
            for j in range(1,m+1):
                if word1[i-1]==word2[j-1]:
                    cur[j]=1+prev[j-1]
                else:
                    cur[j]=max(prev[j],cur[j-1])
            prev=cur
        return n+m -2*(prev[m])