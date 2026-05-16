class Solution:
    def findMin(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                # The minimum is in the right unsorted part
                left = mid + 1
            elif nums[mid] < nums[right]:
                # The right side is sorted, so mid could be the minimum or it's to the left
                right = mid
            else:
                # nums[mid] == nums[right]: duplicate element found. 
                # Safely reduce the search space by shifting the right boundary.
                right -= 1
                
        return nums[left]