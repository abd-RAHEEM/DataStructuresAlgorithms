class Solution(object):
    def leftRightDifference(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        total_sum = sum(nums)
        left_sum = 0
        answer = []
        
        for num in nums:
            # rightSum for index i is: total - leftSum - nums[i]
            right_sum = total_sum - left_sum - num
            
            # Calculate absolute difference
            answer.append(abs(left_sum - right_sum))
            
            # Update left_sum for the next index
            left_sum += num
            
        return answer