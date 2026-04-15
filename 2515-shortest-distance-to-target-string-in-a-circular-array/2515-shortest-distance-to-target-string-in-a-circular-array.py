class Solution(object):
    def closestTarget(self, words, target, startIndex):
        """
        :type words: List[str]
        :type target: str
        :type startIndex: int
        :rtype: int
        """
        n = len(words)
        if target not in words:
            return -1
        
        min_dist = n  # initialize with max possible
        for i, word in enumerate(words):
            if word == target:
                forward = (i - startIndex + n) % n
                backward = (startIndex - i + n) % n
                min_dist = min(min_dist, forward, backward)
        
        return min_dist
