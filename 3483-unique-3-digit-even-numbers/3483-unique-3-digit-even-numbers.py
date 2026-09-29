class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        num_count=Counter(digits)
        valid_count=0
        for num in range(100,1000,2):
            s_num=str(num)
            dig_count=Counter(int(d) for d in s_num)
            possible=True
            for d, freq in dig_count.items():
                if num_count[d]<freq:
                    possible=False
                    break
            if possible:
                valid_count+=1
        return valid_count
        