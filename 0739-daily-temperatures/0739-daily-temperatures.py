class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n=len(temperatures)
        ans=[0]*n
        temp1=[]
        for i,temp in enumerate(temperatures):
            while temp1 and temperatures[temp1[-1]]<temp:
                prev=temp1.pop()
                ans[prev]=i-prev
            temp1.append(i)
        return ans        
