class Solution(object):
    def separateDigits(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        answer = []
        for num in nums:
            # Convert number to string to iterate through digits
            for digit in str(num):
                # Convert character back to int and add to answer
                answer.append(int(digit))
        return answer