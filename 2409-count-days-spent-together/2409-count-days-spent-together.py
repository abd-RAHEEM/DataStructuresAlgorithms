class Solution(object):
    def countDaysTogether(self, arriveAlice, leaveAlice, arriveBob, leaveBob):
        start = max(arriveAlice, arriveBob)
        end = min(leaveAlice, leaveBob)

        if start > end:
            return 0

        md = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

        def days(date):
            m, d = int(date[:2]), int(date[3:])
            return sum(md[:m - 1]) + d

        return days(end) - days(start) + 1