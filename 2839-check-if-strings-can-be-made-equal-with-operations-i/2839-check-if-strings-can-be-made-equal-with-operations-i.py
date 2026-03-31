class Solution(object):
    def canBeEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        even1 = sorted([s1[i] for i in range(0, len(s1), 2)])
        even2 = sorted([s2[i] for i in range(0, len(s2), 2)])
        odd1 = sorted([s1[i] for i in range(1, len(s1), 2)])
        odd2 = sorted([s2[i] for i in range(1, len(s2), 2)])
        return even1 == even2 and odd1 == odd2
