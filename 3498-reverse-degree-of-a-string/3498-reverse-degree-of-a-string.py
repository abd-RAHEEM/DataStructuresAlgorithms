class Solution(object):
    def reverseDegree(self, s):
        """
        :type s: str
        :rtype: int
        """
        revers_arr=[]
        for chars in s:
            revers_arr.append(ord('z')-ord(chars) +1)
        n=len(s)
        ss=0
        for i in range(n):
            ss+=revers_arr[i]*(i+1)
        return ss
        