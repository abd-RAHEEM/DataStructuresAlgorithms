class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        lis=[]
        while n>0:
            h=n%10
            lis.append(h)
            n=n//10
        lis.sort(reverse=True)
        return lis[0]*lis[1]
        