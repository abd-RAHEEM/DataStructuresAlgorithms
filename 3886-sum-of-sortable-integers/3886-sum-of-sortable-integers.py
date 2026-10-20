class Solution(object):
    def sortableIntegers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        s=sorted(nums)
        total_sum=0

        divisors=[]
        for i in range(1,int(n**0.5)+1):
            if n%i==0:
                divisors.append(i)
                if i!=(n//i):
                    divisors.append(n//i)
        for k in divisors:
            valid=True
            for i in range(0,n,k):
                block_nums=nums[i:i+k]
                block_sorted=s[i:i+k]

                if sorted(block_nums)!=block_sorted:
                    valid=False
                    break
                if block_nums[0]==block_nums[-1] and block_nums[0]==block_sorted[0]:
                    continue

                double=block_nums+block_nums

                found=False
                target=block_sorted[0]
                L=len(block_nums)
                for idx, val in enumerate(block_nums):
                    if val==target:
                        if double[idx:idx+L]==block_sorted:
                            found=True
                            break
                if not found :
                    valid=False
                    break
            if valid:
                total_sum+=k
        return total_sum
        
            