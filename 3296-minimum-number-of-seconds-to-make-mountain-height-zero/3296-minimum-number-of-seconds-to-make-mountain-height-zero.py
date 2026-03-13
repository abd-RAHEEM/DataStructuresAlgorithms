class Solution(object):
    def minNumberOfSeconds(self, mountainHeight, workerTimes):
        """
        :type mountainHeight: int
        :type workerTimes: List[int]
        :rtype: int
        """
        def canFinish(T):
            total = 0
            for w in workerTimes:
                x = int((-1 + (1 + 8*T/w)**0.5) // 2)
                total += x
            return total >= mountainHeight

        left, right = 0, min(workerTimes) * mountainHeight * (mountainHeight + 1) // 2
        ans = right
        while left <= right:
            mid = (left + right) // 2
            if canFinish(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
