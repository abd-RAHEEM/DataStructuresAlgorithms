class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """
        arr=[]
        while n>0:
            num=n%10
            if num !=0:
                arr.append(num)
            n=n//10
        if arr==[]:
            return 0
        s=sum(arr)
        num=''
        arr=arr[::-1]
        for i in arr:
            num+=str(i)
        num=int(num)
        return num*s
        