class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s=='' or s==' ':
            return -1
        freq={}
        for char in s:
            freq[char]=freq.get(char,0)+1
        for i ,char in enumerate(s):
            if freq[char]==1:
                return i
        return -1

